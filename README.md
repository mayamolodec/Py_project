# Py_project

### EN version:
#### The challenge: 
Given the user-entered values of the *color index*, metallicity *[Fe/H]*, *log(g)*, calculate the effective temperature of the star *Teff* with these parameters.

Teff calculating pipeline: A third-party program creates a 4D data grid, the dependence of the color indices *J-K*, *J-H*, *H-K*, *J-KS*, *B-V* 
on various parameters, *Teff*, *log(g)* and *[Fe/H]* (all specified with a certain step, not continiously).
***
1. first step of the *log(g)* grid is fixed;

2. a two-dimensional interpolation of the dependence of *Teff* on *[Fe/H]*  and the color index is performed (for this *log(g)* step);

3. the temperature corresponding to the user-entered values of *[Fe/H]* and the **color index** is found;

4. this is repeated for all grid steps of *log(g)* values. The result is the dependence of *Teff* on *log(g)*;

5. a one-dimensional interpolation of the dependence of *Teff* on *log(g)* is performed;

6. The desired effective temperature is found using the *log(g)* value entered by the user;
***
Features of finding the temperature for these models: in the studied temperature range, the dependence on the color index is not unambiguous. The same **color index** value corresponds to 2 different temperatures, so the program has a function that divides this 4D data grid into 2 areas (divided by a point with the maximum *color index* value) - the area of high and low temperatures.

As a result of the program, 2 temperature values (low and high) are output, corresponding to these parameters.

To find out the range in which each of the parameters used is considered, you must enter `-h` when starting, all variables and their maximum and minimum values are described in `help`.

To make the program work, you need to enter in the console: `ph_interp -I` (color index in quotes, for example 'J-K') `-C` (color index value) `-Z` (metallicity from -4 to 1) `-G` (log(g) from 0 to 6)

Example: `ph_interp -I 'J-K' -C 0.15 -Z -3 -G 3`

***
***
### RU version:

Что должна делать программа: по введенным пользователем значениям показателя цвета, _[Fe/H]_, _log(g)_, вычислять эффективную температуру звезды _Teff_ с такими параметрами.

Как производится рассчет температуры: сторонней программой создана 4D сетка данных, зависимость показателей цвета _J-K_, _J-H_, _H-K_,_J-KS_, _B-V_ от различных параметров, _Teff_, _log(g)_ и _[Fe/H]_ (все заданно с определенным шагом). 
***
1. фиксируется определенное значение _log(g)_.

2. производится двумерная интерполяция зависимотси _Teff_ от _[Fe/H]_ и показателя цвета. 

3. находится температура, соответствующая введенным пользователем значениям _[Fe/H]_ и показателя цвета. 

4.  это повторяется для всех значений _log(g)_.В результате получается зависимость _Teff_ от _log(g)_.

5. проводится одномерная интерполяция зависимости _Teff_ от _log(g)_.

6. по введенному пользователем значению _log(g)_ находится искомая эффективная температура.
***
Особенности нахождения температуры для данных моделей: в исследуеммом диапазоне температур зависимость от показателя цвета не является однозначной. Одному и тому же значению показателя цвета соответствуют 2 различные температуры, поэтому в программе написана функция, разделяющая эту 4D сетку данных на 2 области (разделение точкой с максимальным значением показателя цвета) - область высоких и низких температур.

В результате работы программы выводится 2 значения температуры (низкая и высокая), соответствующие данным параметрам.

Чтобы узнать диапазон в котором рассматривается каждый из используеммых параметров необходимо при запуске ввести `-h`, в help описаны все переменные и их максимальные и минимальные значения.

Чтобы программа заработала необходимо в консоли ввести: `ph_interp -I` (показатель цвета в кавычках, например 'J-K') `-С` (значение показателя цвета) `-Z` (металличность от -4 до 1) `-G` (log(g) от 0 до 6)

Пример: `ph_interp -I 'J-K' -C 0.15 -Z -3 -G 3`
