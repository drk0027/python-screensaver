# Tutorial: Escritura de un programa simple de salvapantallas con Python, utilizando programación orientada a objetos. / Te enseño algo que los tutoriales no suelen explicar, creando un protector de pantalla en Python

- [Tutorial: Escritura de un programa simple de salvapantallas con Python, utilizando programación orientada a objetos. / Te enseño algo que los tutoriales no suelen explicar, creando un protector de pantalla en Python](#tutorial-escritura-de-un-programa-simple-de-salvapantallas-con-python-utilizando-programación-orientada-a-objetos--te-enseño-algo-que-los-tutoriales-no-suelen-explicar-creando-un-protector-de-pantalla-en-python)
  - [Introducción](#introducción)
  - [Sobre el aprendizaje desde los fundamentos](#sobre-el-aprendizaje-desde-los-fundamentos)
  - [Estructura del Tutorial](#estructura-del-tutorial)
  - [Requerimientos previos del tutorial](#requerimientos-previos-del-tutorial)
  - [Desarrollo](#desarrollo)
    - [Objeto **«universo.cielo.componentes»**](#objeto-universocielocomponentes)
    - [Objeto **«universo.estrellas.componentes»**](#objeto-universoestrellascomponentes)
    - [Raíz del programa: **«main.py»**](#raíz-del-programa-mainpy)
  - [Flujo del programa](#flujo-del-programa)
    - [Inicialización de clases](#inicialización-de-clases)
  - [Conclusiones](#conclusiones)
- [Webgrafía](#webgrafía)

## Introducción

Como buen principiante que soy, he tenido que deambular buscando tutoriales que me expliquen como hacer ciertas cosas y que resuelven con relativo éxito mis necesidades. Además, mis comienzos en la programación con la universidad fueron muy anticuados, siendo que estudie programación estructurada en lugar de programación orientada a objetos, lo que me dificulta mucho aprender lo ultimo.

Como seguro se habrán dado cuenta, la mayoría de los tutoriales buscan llegar de un punto «A» a un punto «B» sin complicarse mas, para lo que recurren a una forma simple de programación que puede derivar en lo que se conoce como [**«código spaguetti»**](https://es.wikipedia.org/wiki/Código_espagueti), mientras que para aprender programación orientada a objetos, hay que recurrir a textos mecánicos que explican superficialmente y usan ejemplos muy cortos que no aportan demasiado para entender los conceptos.

Este tutorial probablemente no sea el mejor de su tipo, pero mi objetivo es escribir algo que siento que me hubiese servido a entender mejor algunos conceptos, para lo cual he recurrido a un programa escrito en Python por [Suraj Singh](https://www.bitforestinfo.com/blog/04/11/how-to-create-beautiful-movingstars-r-snow-like-screensaver-using-python-and-tkinter.html) quien ha escrito un tutorial breve, pero ha aportado un código super comentado que he traducido, comentado mas y reestructurado para poder explicar algunos conceptos que considero son necesarios para entender mejor sobre Python y programación orientada a objetos.

Quiero aclarar que el tutorial de Suraj Singh no es malo, de hecho, lo considero genial y es la razón por la que lo estoy usando de ejemplo, sino que quiero expandir lo que enseña para cumplir con mis expectativas sobre el aprendizaje desde los fundamentos.

## Sobre el aprendizaje desde los fundamentos

Cuando comenzamos a programar, es muy probable que hayamos empezado por necesidad, por lo cual seguramente habremos buscado con desesperación códigos y los hemos apilado hasta que funcionaran. Esto nos permite aprender muchas cosas y muy rápido, con lo que podemos concluir con éxito lo que nos movió a buscar aprender a programar en primer lugar, pero nos hace confiarnos y descuidar los fundamentos que mas adelante nos permitirían resolver tareas con mas eficiencia y eficacia.

## Estructura del Tutorial

Este tutorial tratará de explicar de forma detallada todos los conceptos requeridos para lograr la creación de un salvapantalla simple escrito en Python. Hay que recordar que **no es un salvapantalla real**, en el sentido de que no puede ser instalado en las plataformas nativas de salvapantallas de Windows o Linux y solo es un modelo básico para explicar los conceptos.

Estará agrupado en dos partes:

- Tutorial documentado con código y gráficos.
- Código comentado, listo para ejecutar.

## Requerimientos previos del tutorial

- Saber escribir un **hola mundo** en Python

Si, solo eso. Hay muchas cosas implicadas en escribir hola mundo en Python, por ejemplo, tener instalado el compilador, saber usar la consola y muchas cosas mas.

Al tener instalado el compilador también se incluyen muchas herramientas y en la mayoría de instalaciones al menos, ya vienen incorporadas las herramientas de Tkinter, para la creación de ventanas en modo gráfico.

Aunque el tutorial puede ser ejecutado en el **«Notepad»** si les parece bien, yo recomiendo el uso de **«Visual Studio Code»**, junto a los complementos de Python, porque tiene funciones de asistencia que facilita depurar e incluso aprender como funcionan las cosas. Si quieres, puedes presionar la tecla _Control_ + _Click izquierdo_ para poder ver la función, clase o variable donde fueron definidas.

## Desarrollo

La programación orientada a objetos, busca la optimización del código mediante el agrupamiento de funciones y atributos conocidos como **«objetos»**. Para entenderlo provisionalmente, he decidido tratar de visualizar, tanto la estructura de carpetas como la organización de funciones, clases y atributos, como objetos del mundo real, por lo que la estructura del directorio representa una caja y la he etiquetado como **_«python screensaver»_**

Dentro de esta caja he creado el primer archivo llamado **«main.py»** que contendrá la lógica del programa y dentro de la misma, he agregado otra caja que he llamado **«universo»**.

    Python permite trabajar con módulos, que no son mas que archivos que contienen código adicional que mantenemos separado del archivo principal para que sea mas fácil de editar y depurar. Durante la ejecución, el interprete unirá todos los archivos en un solo script y los leerá secuencialmente para poder ejecutar el programa en un proceso detallado en el modelo de ejecución, en la documentación oficial.

Para crear un módulo, debemos crear una carpeta que contenga un archivo vacío con nombre **«\_\_init\_\_.py»**. una vez creado, no le volveremos a tocar.

Dado que el programa que estamos escribiendo es un salvapantalla de un cielo estrellado, los nombres de los módulos deberían reflejar esto, por lo que la carpeta universo contendrá al cielo, con sus funciones(o sea, el código que define su comportamiento) y atributos y a las estrellas, también con sus funciones y atributos. _(Podríamos ignorar un poco el debate de si el cielo contiene a las estrellas o el universo contiene al cielo)_. Esto deja nuestro directorio de la siguiente manera:

![Jerarquía archivos Python screensaver](https://interlan.ec/wp-content/uploads/Jerarquia-archivos-python-screensaver.png)

Es recomendable que cada parte del código sea **fácil de entender**, que cada nombre y variable sea **fácil de deducir** y todo este muy bien ordenado porque, aunque al inicio funcione, si hay que modificar o corregir mas adelante, puede llegar a ser muy complicado y enigmático. Es por eso que en esta ocasión he elegido este esquema para los nombres de carpetas y módulos. Por supuesto, si se desea se puede usar cualquier esquema, no hay reglas estrictas en este sentido.

**Nota:** Usualmente el primer archivo de tu código debería llamarse **«main.py»**, puesto que este es el nombre mas frecuentemente usado para indicar que todo el programa comienza por allí, pero en otros lenguajes de programación, como JavaScript(con NodeJS), se llaman **«index.js»**. Esto no es estrictamente necesario puesto que el primer archivo puede tomar cualquier nombre. Solo es un acuerdo tácito entre programadores para facilitar la lectura del código.

En el archivo **«main.py»** vamos a comenzar haciendo nuestras primeras importaciones de módulos del sistema:

    import tkinter as tk
    import time
    import random

Los módulos se pueden importar por su nombre, pero durante la escritura del código, tal vez prefieras utilizar un **«alias»** o apodo, para reducir la cantidad de texto al escribir. En mi caso he importado el módulo _tkinter_ como _tk_, pero en otros tutoriales pueden optar por otros nombres. Por supuesto, también puedes importarlo sin ningún alias, no hay problema con eso y como ves, la mayor parte de los módulos aquí usados aparte de **tkinter**, se usan de esa manera.

Nuestro salvapantalla tiene que preparar algunas cosas antes de visualizarse, por lo que nuestro siguiente componente en ser cargado es la clase **«cielo»** dentro del módulo **«universo»**.

Cuando creamos nuestra estructura de archivos, consideramos la carpeta **«Python screensaver»** como nuestro contenedor y dentro del mismo, creamos la carpeta **«universo»**.

Al definir el archivo **«\_\_init\_\_.py»**, la carpeta pasa a ser parte del módulo, por lo que al importar el objeto «cielo», la buscará en el módulo universo, según este esquema:

    import nombre_módulo.nombre_objeto

Así que importaríamos nuestro módulo de la siguiente manera:

    import universo.cielo

Nuestro trabajo ahora consiste en desarrollar el objeto **«cielo.componentes»**.

En el módulo cielo debemos repetir la importación de los módulos, pero en este caso solo hace falta uno:

    import tkinter as tk

Además, importaremos también el otro objeto creado en el módulo universo llamado estrellas.

    import universo.estrellas

### Objeto **«universo.cielo.componentes»**

Según la [Wikipedia](https://es.wikipedia.org/wiki/Objeto_(programación)):

    Un objeto es un ente orientado a objetos (programa de computadoras) que consta de un estado y de un comportamiento, que a su vez constan respectivamente de datos almacenados y de tareas realizables durante el tiempo de ejecución. Un objeto puede ser creado instanciando una clase, como ocurre en la programación orientada a objetos, o mediante escritura directa de código y la replicación de otros objetos, como ocurre en la programación basada en prototipos.

En nuestro caso, los atributos de nuestro módulo **«cielo»** se encuentran en nuestra clase **«componentes»** donde está definida una función que establece los parámetros iniciales de funcionamiento y variables que contienen sus atributos **(def \_\_init\_\_(self, \*args, \*\*kwargs))** y dos funciones que definen el comportamiento del cielo **(def crear_estrellas(self) y def actualizar_pantalla(self))** 

El código de la clase **«universo.cielo.componentes»** queda entonces de la siguiente manera:

    import tkinter as tk
    import universo.estrellas

    CANTIDAD_ESTRELLAS = 2

    class componentes(tk.Canvas):
        def __init__(self, *args, **kwargs):
            tk.Canvas.__init__(self, *args, **kwargs) 
            self.estrellas = []
            self.crear_estrellas()

    def crear_estrellas(self):
        for i in range(CANTIDAD_ESTRELLAS):
            self.estrellas.append(universo.estrellas.componentes(self))
        return

    def actualizar_pantalla(self):
        for i in self.estrellas:
            i.actualizar()
        return

### Objeto **«universo.estrellas.componentes»**

    Nota: No hay una forma lineal de escribir código en cuanto a programación orientada a objetos se refiere. Como te has dado cuenta, hasta el momento hemos creado una clase y ahora crearemos otra clase, ninguna de las cuales puede ser ejecutadas individualmente. Nuestro archivo «main.py» continua vacío excepto algunas importaciones que agregamos al principio. Esto es debido a que el código ya ha pasado por algunas pruebas y esquematizaciones, lo que permite crear este código ya organizado.
    
    Es cuestión del programador el determinar la mejor forma de escribir su código, pero para practicar te recomiendo escribir programas sencillos en un solo archivo y practicar luego modularizándolos y convirtiendo en objetos algunas funciones y variables. Lo importante es entender los conceptos antes de tirarse a un proyecto mas grande, aunque si han llegado a este tutorial, es probable que ya hayan puesto en marcha algo de código antes de entender como funciona.

Al igual que en el módulo anterior, hacemos las respectivas importaciones, creamos las variables globales y creamos la clase:

    import random

    VELOCIDAD_RADIO=[i/10.0 for i in range(-10,-2)]+[i/10.0 for i in range(2,10)]
    RADIO=25
    COLOR_ESTRELLA = "yellow"

    class componentes:
        def __init__(self, padre):
            self.padre = padre
            self.comenzar_movimiento()
            self.crear_circulo_pequeño()
        
        def comenzar_movimiento(self):
            self.x1 = self.padre.winfo_width()/2
            self.y1 = self.padre.winfo_height()/2
            self.velocity_x = random.choice(VELOCIDAD_RADIO)
            self.velocity_y = random.choice(VELOCIDAD_RADIO)
            return

        def crear_circulo_pequeño(self):
            x1=self.x1
            y1=self.y1
            x2,y2=x1+RADIO, y1+RADIO
            self.estrella = self.padre.create_oval(x1,y1,x2,y2, fill=COLOR_ESTRELLA)
            return

        def parar_movimiento(self):
            self.padre.coords(self.estrella, self.x1,self.y1,self.x1+RADIO,self.y1+RADIO)
            self.comenzar_movimiento()
            return

        def actualizar(self):
            self.padre.move(self.estrella, self.velocity_x, self.velocity_y)
            x,y = self.padre.coords(self.estrella)[:2]
            if x<0 or x>1500:
                self.parar_movimiento()
            elif y<0 or y>1000:
                self.parar_movimiento()
            return

### Raíz del programa: **«main.py»**

Podría parecer un poco extraño no haber comenzado desde el inicio, pero el objetivo de este tutorial no es explicar el diseño de un código modular, sino explicar los conceptos implicados en el desarrollo del código mediante programación orientada a objetos. Debido a esto, recién llegamos a la parte que unificará todo el código escrito hasta el momento.

El código entonces, quedaría así:

    import tkinter as tk
    import time
    import random
    import universo.cielo

    COLOR_FONDO="black"
    NIVEL_TRANSPARENCIA=1
    EVENTOS_DE_CIERRE = ['<Any-KeyPress>', '<Any-Button>']

    def main():
        raiz=tk.Tk()#establecer la ventana raiz o inicial

        pantalla=universo.cielo.componentes(raiz,bg=COLOR_FONDO)
        pantalla.pack(expand="yes",fill="both") 
        
        raiz.wait_visibility(pantalla)
        raiz.wm_attributes('-alpha',NIVEL_TRANSPARENCIA)
        raiz.wm_attributes("-topmost", True)
        raiz.overrideredirect(1)
        raiz.state('zoomed')

        def salir(event):
            raiz.destroy()
            return
        
        for seq in EVENTOS_DE_CIERRE:
            raiz.bind_all(seq, salir)

        while True:
            raiz.update()
            raiz.update_idletasks()
            pantalla.actualizar_pantalla()

    if __name__ == '__main__':
    main()

## Flujo del programa

El código ya se encuentra completamente comentado y explicando que hace cada función, variable, clase y modulo, pero hare unas cuantas aclaraciones aquí.

### Inicialización de clases

Importar los módulos no es suficiente para empezar a usarlos. Es necesario inicializarlos, para lo cual, se los llama solos o dentro de una variable, pasándoles los parámetros necesarios para funcionar.

El modulo «universo.cielo.componentes» es inicializada en la función «main()» del archivo main.py de la siguiente manera:

    pantalla=universo.cielo.componentes(raiz,bg=COLOR_FONDO)

La clase **«universo.cielo.componentes»** recibe como parámetro, la inicialización que hemos realizado del componente **«tkinter»**. Esto nos evita tener que inicializar las clases y redefinir nuestros parámetros cada vez que lo necesitemos. Reutilizar código es una de las piezas clave de la **Programación Orientada a Objetos** y en este caso, lo que haremos se conoce como **«Herencia»**

La clase **«universo.cielo.componentes»** recibe los parámetros e inicializa las variables y funciones necesarias. Es decir, crea una instancia de la ventana que hemos creado, crea un arreglo que contendrá las estrellas e inicializara la función «crear_estrellas()» para definir el comportamiento inicial de la clase.

    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs) 
        self.estrellas = []
        self.crear_estrellas()

En Python, se utiliza la palabra **«self»** para representar una instancia de la clase. Esto le permite acceder a los atributos y funciones que esta posee. Todas las funciones definidas en la clase, deberán utilizar esta palabra para poder acceder a sus variables inicializadas en **«\_\_init\_\_»**

El arreglo **«self.estrellas»** no contendrá datos, sino instancias de la siguiente clase que vamos a inicializar: **«universo.estrellas.componentes»**

La función **«crear_estrellas()»** crea un ciclo donde se agregan diferentes instancias de la clase **«universo.estrellas.componentes»** de acuerdo a la cantidad que hayamos definido en la variable **«CANTIDAD_ESTRELLAS»**

    def crear_estrellas(self):
        for i in range(CANTIDAD_ESTRELLAS):
            self.estrellas.append(universo.estrellas.componentes(self))
        return

Las clases son instanciadas cada vez que son invocadas. En el caso de **«universo.estrellas.componentes»**, sera instanciada 2 veces según lo definido en **«CANTIDAD_ESTRELLAS»**, lo cual significa que el objeto estrella llega a existir dos veces, lo cual es equivalente a tener físicamente dos estrellas, con sus respectivos atributos y comportamiento.

La clase **«universo.estrellas.componentes»**, al momento de ser inicializada, heredará todos los atributos de la clase que la llama, estableciéndose una relación **«Padre-Hija»** Esto se logra enviando como parámetro la palabra **«self»** y recibiéndola en una variable que en este caso llamaremos **«self.padre»**

    def __init__(self, padre):
       self.padre = padre
       self.comenzar_movimiento()
       self.crear_circulo_pequeño()

La clase **«universo.estrellas.componentes»** al ser inicializada, guarda la información de la clase padre en la variable **«self.padre»** y llama dos funciones: «self.comenzar_movimiento()» y «self.crear_circulo_pequeño()». Estas funciones establecen los parámetros iniciales del objeto en la pantalla y crean el objeto en la pantalla.

Una vez inicializadas las clases, la función **«main()»** tiene acceso completo a sus atributos y funciones, por lo cual, se procede a actualizarlas desde el _loop_**«While True»**

    while True:
        raiz.update() 
        raiz.update_idletasks()
        pantalla.actualizar_pantalla()

La variable **«pantalla»** ahora tiene acceso a la función **«actualizar_pantalla()»** dentro de la clase **«universo.cielo.componentes»** la cual hará un barrido de los objetos creados en «self.estrellas» para que actualicen sus propiedades.

**«universo.cielo.componentes.actualizar_pantalla()»**

    def actualizar_pantalla(self):
        for i in self.estrellas:
            i.actualizar()
        return

**«universo.estrellas.componentes.actualizar()»**

    def actualizar(self):
        self.padre.move(self.estrella, self.velocity_x, self.velocity_y)
        x,y = self.padre.coords(self.estrella)[:2]
        if x<0 or x>1500:
            self.parar_movimiento()
        elif y<0 or y>1000:
            self.parar_movimiento()
        return

## Conclusiones

La **programación orientada a objetos** puede ser muy confusa a veces. Como hemos visto, un programa relativamente sencillo puede ser un laberinto difícil de rastrear, sin embargo, nos permite realizar cosas complejas de forma mas eficiente.

Entender la programación orientada a objetos desde su enfoque inicial, como una representación de los objetos de la vida real, puede facilitar mucho las cosas. Es de sentido común que todo objeto que nos rodea, tiene atributos y comportamientos definidos, pero es un poco mas abstracto los conceptos de herencia, abstracción, polimorfismo, acoplamiento y encapsulamiento, pero es un buen punto de partida.

Conforme se siga practicando, es posible entender cosas mas complejas y también es posible llegar a entender, por que se hizo tan popular en la actualidad.

# Webgrafía

Módulos en Python. Por Learn Python. [https://www.learnpython.org/es/Modules%20and%20Packages](https://www.learnpython.org/es/Modules%20and%20Packages)

how to create beautiful moving stars/snow like screen saver using python and tkinter - tutorial - two | python gui example. Por Suraj Singh. [https://www.bitforestinfo.com/blog/04/11/how-to-create-beautiful-movingstars-r-snow-like-screensaver-using-python-and-tkinter.html](https://www.bitforestinfo.com/blog/04/11/how-to-create-beautiful-movingstars-r-snow-like-screensaver-using-python-and-tkinter.html)

Objeto(programación) [https://es.wikipedia.org/wiki/Objeto_(programación)](https://es.wikipedia.org/wiki/Objeto_(programación))

Código Espagueti [https://es.wikipedia.org/wiki/Código_espagueti](https://es.wikipedia.org/wiki/Código_espagueti)

Modelo de Ejecución [https://docs.python.org/es/3/reference/executionmodel.html](https://docs.python.org/es/3/reference/executionmodel.html)

Herencia (informática)[https://es.wikipedia.org/wiki/Herencia_(inform%C3%A1tica)](https://es.wikipedia.org/wiki/Herencia_(inform%C3%A1tica))