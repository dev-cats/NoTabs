import click


@click.command()
@click.argument('file', type=click.Path(exists=True))
@click.option('-w', '--width', type=int, default=4, help='tab size')
def cli(file, width):
    buf = ''
    with open(file) as f:
        with click.progressbar(f, label='Reading...', color='red') as bar:
            for i in bar:
                s = i.lstrip('\t')
                buf += ' ' * width * (len(i) - len(s)) + s
    with open(file, 'w') as f:
        with click.progressbar(buf, label='Writing...', color='green') as bar:
            for i in bar:
                f.write(i)
    click.echo('Done!')
