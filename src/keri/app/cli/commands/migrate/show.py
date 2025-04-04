# -*- encoding: utf-8 -*-
"""
keri.kli.commands module

"""
import argparse

from hio.base import doing

from keri import help
from keri.app.cli.common import existing

logger = help.ogler.getLogger()


def handler(args):
    """
    Launch KERI database initialization

    Args:
        args(Namespace): arguments object from command line
    """
    clean = CleanDoer(args)
    return [clean]


parser = argparse.ArgumentParser(description='Cleans and migrates a database and keystore')
parser.set_defaults(handler=handler,
                    transferable=True)

# Parameters for basic structure of database
parser.add_argument('--name', '-n', help='keystore name and file location of KERI keystore', required=True)
parser.add_argument('--base', '-b', help='additional optional prefix to file location of KERI keystore',
                    required=False, default="")
parser.add_argument('--temp', '-t', help='create a temporary keystore, used for testing', default=False)
parser.add_argument('--migration', '-m', help='migration name', required=True)


# Parameters for Manager creation
# passcode => bran
parser.add_argument('--passcode', '-p', help='21 character encryption passcode for keystore (is not saved)',
                    dest="bran", default=None)


class CleanDoer(doing.Doer):

    def __init__(self, args):
        self.args = args
        super(CleanDoer, self).__init__()

    def recur(self, tyme):
        hby = existing.setupHby(name=self.args.name, base=self.args.base,
                                bran=self.args.bran, temp=self.args.temp)

        [(name, dater)] = hby.db.complete(name=self.args.migration)
        date = dater.datetime.strftime("%Y-%m-%d %H:%M") if dater is not None else "Not Run"

        print(f"{self.args.migration} -> {date}")

        return True
