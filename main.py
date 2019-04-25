from time import sleep
import click


@click.command()
@click.argument('file', type=click.Path(exists=True))
@click.option('-w', '--width', type=int, default=4, help='tab size')
def cli(file, width):
    buf = ''
    with open(file) as f:
        r = f.readlines()

        with click.progressbar(r, length=len(r), label=click.style('Reading...', reset=False), color=True) as bar:
            sleep(.5)
            for i in bar:
                s = i.lstrip('\t')
                buf += ' ' * width * (len(i) - len(s)) + s
    with open(file, 'w') as f:
        with click.progressbar(buf, label=click.style('Writing...', reset=False), color=True) as bar:
            sleep(.5)
            for i in bar:
                f.write(i)
    click.echo('Done!')
