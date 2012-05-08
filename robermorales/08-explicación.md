La manera más rápida de resolver el problema es codificar el funcionamiento de la máquina. Pero no es la manera más eficiente. La manera más eficiente es, primero, reducir todas las iteraciones de la máquina a una sola, y, entonces, aplicarla una sóla vez.

Para reducir las transformaciones de la máquina usamos un dict que comienza siendo la transformación identidad:
	
	{
		'a' : 'a',
		'b' : 'b',
		...
	}
	
Si aplicamos las transformaciones indicadas en la entrada de forma sucesiva, pero no a la cola inicial, sino al propio conjunto de transformaciones, estaremos transformando un problema que podría ser ilimitado (no conocemos el tamaño de la cola) por un problema de complejidad casi lineal (el conjunto de transformaciones es siempre del mismo tamaño, un elemento por cada letra). La idea es razonar sobre las transformaciones y, cuando estén todas expresadas en un único conjunto, aplicarla una sóla vez.

Si aplicamos las transformaciones indicadas sobre el conjunto actual de forma incremental, nos encontraremos con la función replace:
	
	for i,a in tl.iteritems():
		tl[ i ] = a.replace( ... )
	...
	
La función replace es lenta y podemos optimizar este comportamiento recorriendo las líneas en sentido inverso. Así, volvemos a convertir un problema de tamaño desconocido en otro casi acotado. Ejemplo

	a=>bc
	b=>def
	c=>ghi

Paso 1 (identidad):
	
	a=>a,b=>b,...

Paso 2 (última línea):
	
	a=>a,b=>b,c=>ghi

Paso 3 (penúltima línea):

	a=>a,b=>def,c=>ghi

Paso 4 (primera línea y momento clave):
	
	a=>defghi,b=>def,c=>ghi

En este momento aplicamos la transformación, pero, por supuesto, no concatenamos el resultado, sino que simplemente vamos haciendo update sobre el MD5 ya que la cadena resultante no la llegamos a necesitar para nada.

Hay tres operaciones costosas clave: buscar y reemplazar. Se trata de sustituirlas por recorrer listas y concatenar, y esto se consigue dando la vuelta a las líneas.


