# Conway-s-Game-of-Life
Conway's Game of Life made with Python. It also provides a chart with the information of born, dead and alive cells on the board.

Este problema consiste de crear un programa en Python que simule el juego de la vida de Conway. \\
Las reglas de este juego son:
\begin{itemize}
    \item \textbf{Sobrevivientes: }Cada célula con dos o tres vecinos sobrevive para la próxima generación.
    \item \textbf{Muertes: }
    \begin{itemize}
        \item[-] Cada  célula con cuatro o más vecinos muere (es eliminado) debido a sobre-población.
        \item[-] Cada célula con un vecino o menos, muere por aislamiento.
    \end{itemize}
    \item \textbf{Nacimiento: }Cada celda vacía, adyacente a exactamente tres vecinos es un nueva célula, que se ubica en la celda para la próxima generación.
\end{itemize}

Debe crear un tablero de tamaño $n\times n$ y a partir de $N_0$ células iniciales, ubicadas aleatoriamente, debe iniciar el juego. A partir de esto, y con un parámetro de entrada $m$, donde $m$ es el número de generaciones a mostrar, debe:
\begin{itemize}
    \item Mostrar un gráfico donde se vea el número de vivos, nacimientos y muertes en cada generación.
    \item Mostrar por medio de una interfaz gráfica cada generación. Es decir, animar el estado del tablero, incluyendo botones de pausar/continuar.
\end{itemize}
