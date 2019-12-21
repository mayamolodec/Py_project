#!/usr/bin/python3
# coding: utf-8

import numpy as np
from astropy.io import fits
from scipy import interpolate
from scipy.interpolate import griddata
import argparse


def sort(Col_ind, log_z, Teff, log_g):
	""" Функция сортирует массивы содержащие значения 
		Teff, Log(g), [Fe/H], показателя цвета по массиву Teff """

	x = zip(Col_ind, log_z, Teff, log_g)
	xs = sorted(x, key=lambda tup: tup[2])
	Col_ind_fin = [x[0] for x in xs]
	log_z_fin = [x[1] for x in xs]
	Teff_fin = [x[2] for x in xs]
	log_g_fin = [x[3] for x in xs]

	return np.array(Col_ind_fin), np.array(log_z_fin), np.array(Teff_fin), np.array(log_g_fin)


def mask(Col_ind, log_z, Teff, log_g, i):
	""" Функция выделяет из массивов содержащих значения 
		Teff, [Fe/H], показателя цвета элементы соответствующие заданному Log(g) """

	mask = (log_g == i)
	Col_ind_fin = Col_ind[(mask)]
	log_z_fin = log_z[(mask)]
	Teff_fin = Teff[(mask)]

	return Col_ind_fin, log_z_fin, Teff_fin


def cut_hot(Col_ind, log_z, Teff, Zi):
	""" Из-за того, что зависимость Teff от показателя цвета неоднозначная 
		(один и тот же показатель цвета может соответствовать разным температурам),
		необходимо разделить массивы содержащие значения показателя цвета, Teff, [Fe/H] 
		на область низких и высоких температур. Функция находит максимальное значение показателя цвета
		и выделяет из массивов элементы соответствующие большим температурам """

	COLIND = []
	ZVAL = []
	TEFF = []

	for i in Zi:
		mask = (log_z == i)
		Col_ind_f = Col_ind[(mask)]
		Teff_f = Teff[(mask)]

		ind = np.argmax(Col_ind_f)
		Col_ind_f = Col_ind_f[ind:]
		Teff_f = Teff_f[ind:]

		COLIND = np.concatenate((COLIND, Col_ind_f))
		TEFF = np.concatenate((TEFF, Teff_f))
		zval = np.ones((len(Col_ind_f)))*i
		ZVAL = np.concatenate((ZVAL, zval))

	return COLIND, ZVAL, TEFF


def cut_cold(Col_ind, log_z, Teff, Zi):
	""" Из-за того, что зависимость Teff от показателя цвета неоднозначная 
		(один и тот же показатель цвета может соответствовать разным температурам),
		необходимо разделить массивы содержащие значения показателя цвета, Teff, [Fe/H] 
		на область низких и высоких температур. Функция находит максимальное значение показателя цвета
		и выделяет из массивов элементы соответствующие низким температурам """

	COLIND = []
	ZVAL = []
	TEFF = []
	
	for i in Zi:
		mask = (log_z == i)
		Col_ind_f = Col_ind[(mask)]
		Teff_f = Teff[(mask)]
		
		ind = np.argmax(Col_ind_f)
		Col_ind_f = Col_ind_f[:ind]
		Teff_f = Teff_f[:ind]

		COLIND = np.concatenate((COLIND, Col_ind_f))
		TEFF = np.concatenate((TEFF, Teff_f))
		zval = np.ones((len(Col_ind_f)))*i
		ZVAL = np.concatenate((ZVAL, zval))

	return COLIND, ZVAL, TEFF


def interp_1D(new_grid, old_grid, old_func, val):
	""" Функция производит одномерную интерполяцию, и возвращает значение функции, 
	соответствующее заданному пользователем параметру """
	
	res = np.interp(new_grid, old_grid, old_func)
	mas = np.argmin(np.abs(new_grid-val))

	return np.round(res[mas],3)

def interp_2D(x, y, z, Col_i, log_z_val):
		x_grid = np.around(np.arange(round(np.min(x), 3), round(np.max(x), 3)+0.001, 0.001), 3)
		y_grid = np.around(np.arange(np.min(y), np.max(y)+0.01, 0.01), 2)

		X, Y = np.meshgrid(x_grid, y_grid, indexing='xy')
		Z = griddata((x, y), z, (X, Y), method='linear')

		mas_x = np.argmin(np.abs(x_grid - Col_i))
		mas_y = np.argmin(np.abs(y_grid - log_z_val))

		return np.round(np.float(Z[mas_x, mas_y]), 3)


def main(Col_ind_val, Col_i, log_z_val, log_g_val):
	""" Функция main() открывает fits-файл с массивами содержащими значения 
	Teff, Log(g), [Fe/H] и различных показателей цвета. Далее проводится двумерная интерполяция этих данных.
	В результате работы программы пользователь получает на выходе значение эффективной температуры звезды, 
	соответствующее введенным им значениям Log(g), [Fe/H] и показателя цвета """

	a = fits.open('Phoenix.fits')

	Teff = a[1].data.field(0)
	log_g = a[1].data.field(1)
	log_z = a[1].data.field(2)
	J_K = a[1].data.field(3)
	J_H = a[1].data.field(4)
	H_K = a[1].data.field(5)
	J_KS = a[1].data.field(6)
	B_V = a[1].data.field(7)

	logg = np.arange(0, 6.5, 0.5)
	g_grid = np.arange(0, 6.5, 0.01)
	Fe_H = np.array([-4, -3, -2, -1.5, -1, -0.5, 0, 0.5, 1])

	if Col_ind_val == 'J-K':
		Col_ind = J_K
	elif Col_ind_val == 'J-H':
		Col_ind = J_H
	elif Col_ind_val == 'H-K':
		Col_ind = H_K
	elif Col_ind_val == 'J-KS':
		Col_ind = J_KS
	elif Col_ind_val == 'B-V':
		Col_ind = B_V
	else:
		print('Error! Choose another color index')

	Col_ind_s, log_z_s, Teff_s, log_g_s = sort(Col_ind, log_z, Teff, log_g)

	Num = 0
	log_g_step = np.zeros((13))
	log_g_step2 = np.zeros((13))

	for i in logg:
		Col_ind_fin, log_z_fin, Teff_fin = mask(Col_ind_s, log_z_s, Teff_s, log_g_s, i)
		x, y, z = cut_hot(Col_ind_fin, log_z_fin, Teff_fin, Fe_H)
		x2, y2, z2 = cut_cold(Col_ind_fin, log_z_fin, Teff_fin, Fe_H)

		result = interp_2D(x, y, z, Col_i, log_z_val)
		result2 = interp_2D(x2, y2, z2, Col_i, log_z_val)

		log_g_step[Num] = result
		log_g_step2[Num] = result2

		Num = Num+1

	Teff_hot = interp_1D(g_grid, logg, log_g_step, log_g_val)
	Teff_cold = interp_1D(g_grid, logg, log_g_step2, log_g_val)

	return  Teff_hot, Teff_cold


if __name__=='__main__':
	parser = argparse.ArgumentParser(prog='Phoenix_interpol.py')

	parser.add_argument("-I", "--color_name", type=str,
	                    help="String whith the name of your color index:'J-K', 'J-H', 'H-K', 'J-KS', B-V'")
	parser.add_argument("-C", "--color_value", type=float,
	                    help="The value of your color index")
	parser.add_argument("-Z", "--metall", type=float,
	                    help="Metallisity of your star, changes in range -4 to 1")
	parser.add_argument("-G", "--log_g", type=float,
	                    help="Log(g) of your star, changes in range 0 to 6")

	args = parser.parse_args()

	teff1, teff2 = main(Col_ind_val=args.color_name, Col_i=args.color_value, log_z_val=args.metall, log_g_val=args.log_g)
	print('For hot star:', teff1, 'K', '\nFor cold star', teff2, 'K')