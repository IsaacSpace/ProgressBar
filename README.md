# ProgressBar

ProgressBar es una utilidad para controlar el tiempo de ejecución de diversos procesos. Su uso es sencillo y se puede utilizar en alguna tarea que haga uso de ciclos for o while. Ejemplo de uso:

```python
    from progressbar import ProgressBar

    pbar = ProgressBar(max = 100, iterator = "#", message = "Cargando")

    pbar.start()
    for i in range(0, 100, 1):
        pbar.step()

    pbar.end()
```
