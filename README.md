# Conway-s-Game-of-Life
Conway's Game of Life made with Python. It also provides a chart with the information of born, dead and alive cells on the board.
<p>Este problema consiste de crear un programa en Python que simule el juego de la vida de Conway.<br />
Las reglas de este juego son:</p>
<ul>
<li><p><strong>Sobrevivientes:</strong> Cada célula con dos o tres vecinos sobrevive para la próxima generación.</p></li>
<li><p><strong>Muertes:</strong></p>
<ul>
<li><p>Cada célula con cuatro o más vecinos muere (es eliminado) debido a sobre-población.</p></li>
<li><p>Cada célula con un vecino o menos, muere por aislamiento.</p></li>
</ul></li>
<li><p><strong>Nacimiento:</strong> Cada celda vacía, adyacente a exactamente tres vecinos es un nueva célula, que se ubica en la celda para la próxima generación.</p></li>
</ul>
<p>Debe crear un tablero de tamaño <span class="math inline">\(n\times n\)</span> y a partir de <span class="math inline">\(N_0\)</span> células iniciales, ubicadas aleatoriamente, debe iniciar el juego. A partir de esto, y con un parámetro de entrada <span class="math inline">\(m\)</span>, donde <span class="math inline">\(m\)</span> es el número de generaciones a mostrar, debe:</p>
<ul>
<li><p>Mostrar un gráfico donde se vea el número de vivos, nacimientos y muertes en cada generación.</p></li>
<li><p>Mostrar por medio de una interfaz gráfica cada generación. Es decir, animar el estado del tablero, incluyendo botones de pausar/continuar.</p></li>
</ul>
