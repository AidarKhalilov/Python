from sys import modules

# Задача 1. Приведите примеры кода, которые соответствуют нарушениям PEP 8:
# 1. вызов функции foo ()
# 2. a+b
# 3. foo(a,b)
# 4. print(something, sep = ' ')
# 5. 2 строчки между определениями функций
# 6. if x > 5: y = 10
# 7. a = 5; b = 7
# 8. if something == None
# 9. if something == True


# Задача 2. Как вы думаете, модуль загружается один раз или загружается каждый раз при очередном импорте?
# Докажите правильность вашей гипотезы кодом.
# Модули Python не импортируются несколько раз, поэтому повторное выполнение команды оператора импорта не приведет к
# перезагрузке модуля. Если вы хотите, чтобы он был перезагружен, вам необходимо выполнить инструкцию reload.


# Задача 3. GLOBAL VARIABLE относится только к одному пользователю