# -*- encoding: utf-8 -*-
"""
KERI
keri.base.directing module

simple direct mode demo support classes
"""
import json

from hio.base import doing, tyming
from hio.core.tcp import clienting, serving
from .. import kering
from ..db import dbing
from ..core import coring, eventing
from ..base import keeping, directing

from .. import help

logger = help.ogler.getLogger()


class BobDirector(directing.Director):
    """
    Direct Mode KERI Director (Contextor, Doer) with TCP Client and Kevery
    Generator logic is to iterate through initiation of events for demo

    Inherited Attributes:
        .hab is Habitat instance of local controller's context
        .client is TCP client instance. Assumes operated by another doer.

    Attributes:

    Inherited Properties:
        .tyme is float relative cycle time, .tyme is artificial time
        .tock is desired time in seconds between runs or until next run,
                 non negative, zero means run asap

    Properties:

    Inherited Methods:
        .__call__ makes instance callable return generator
        .do is generator function returns generator

    Methods:

    Hidden:
       ._tymist is Tymist instance reference
       ._tock is hidden attribute for .tock property
    """

    def do(self, tymist, tock=0.0, **opts):
        """
        Generator method to run this doer
        Calling this method returns generator
        """
        try:
            # enter context
            self.wind(tymist)  # change tymist and dependencies
            self.tock = tock
            tyme = self.tyme

            # recur context
            tyme = (yield (self.tock))  # yields tock then waits for next send

            logger.info("**** %s:\nWaiting for connection to remote  %s.\n\n", self.hab.pre, self.client.ha)
            while (not self.client.connected):
                tyme = (yield (self.tock))

            logger.info("**** %s:\nConnected to %s.\n\n", self.hab.pre, self.client.ha)

            self.sendOwnInception()  # Inception Event
            tyme = (yield (self.tock))

            msg = self.hab.rotate()  # Rotation Event
            self.client.tx(msg)   # send to connected remote
            logger.info("**** %s:\nSent event:\n%s\n\n", self.hab.pre, bytes(msg))
            tyme = (yield (self.tock))

            msg = self.hab.interact()  # Interaction event
            self.client.tx(msg)   # send to connected remote
            logger.info("**** %s:\nSent event:\n%s\n\n", self.hab.pre, bytes(msg))
            tyme = (yield (self.tock))

        except GeneratorExit:  # close context, forced exit due to .close
            pass

        except Exception:  # abort context, forced exit due to uncaught exception
            raise

        finally:  # exit context,  unforced exit due to normal exit of try
            pass

        return True # return value of yield from, or yield ex.value of StopIteration


class SamDirector(directing.Director):
    """
    Direct Mode KERI Director (Contextor, Doer) with TCP Client and Kevery
    Generator logic is to iterate through initiation of events for demo

    Inherited Attributes:
        .hab is Habitat instance of local controller's context
        .client is TCP client instance. Assumes operated by another doer.

    Attributes:

    Inherited Properties:
        .tyme is float relative cycle time, .tyme is artificial time
        .tock is desired time in seconds between runs or until next run,
                 non negative, zero means run asap

    Properties:

    Inherited Methods:
        .__call__ makes instance callable return generator
        .do is generator function returns generator

    Methods:

    Hidden:
       ._tymist is Tymist instance reference
       ._tock is hidden attribute for .tock property
    """

    def do(self, tymist, tock=0.0, **opts):
        """
        Generator method to run this doer
        Calling this method returns generator
        """
        try:
            # enter context
            self.wind(tymist)  # change tymist and dependencies
            self.tock = tock
            tyme = self.tyme

            # recur context
            tyme = (yield (self.tock))  # yields tock then waits

            while (not self.client.connected):
                logger.info("%s:\n waiting for connection to remote %s.\n\n",
                            self.hab.pre, self.client.ha)
                tyme = (yield (self.tock))

            logger.info("%s:\n connected to %s.\n\n", self.hab.pre, self.client.ha)

            self.sendOwnInception()  # Inception Event
            tyme = (yield (self.tock))

            msg = self.hab.interact()  # Interaction Event
            self.client.tx(msg)  # send to connected remote
            logger.info("%s sent event:\n%s\n\n", self.hab.pre, bytes(msg))
            tyme = (yield (self.tock))

            msg = self.hab.rotate()  # Rotation Event
            self.client.tx(msg)  # send to connected remote
            logger.info("%s sent event:\n%s\n\n", self.hab.pre, bytes(msg))
            tyme = (yield (self.tock))

        except GeneratorExit:  # close context, forced exit due to .close
            pass

        except Exception:  # abort context, forced exit due to uncaught exception
            raise

        finally:  # exit context,  unforced exit due to normal exit of try
            pass

        return True  # return value of yield from, or yield ex.value of StopIteration


class EveDirector(directing.Director):
    """
    Direct Mode KERI Director (Contextor, Doer) with TCP Client and Kevery
    Generator logic is to iterate through initiation of events for demo

    Inherited Attributes:
        .hab is Habitat instance of local controller's context
        .client is TCP client instance. Assumes operated by another doer.

    Attributes:

    Inherited Properties:
        .tyme is float relative cycle time, .tyme is artificial time
        .tock is desired time in seconds between runs or until next run,
                 non negative, zero means run asap

    Properties:

    Inherited Methods:
        .__call__ makes instance callable return generator
        .do is generator function returns generator

    Methods:

    Hidden:
       ._tymist is Tymist instance reference
       ._tock is hidden attribute for .tock property
    """

    def do(self, tymist, tock=0.0, **opts):
        """
        Generator method to run this doer
        Calling this method returns generator
        """
        try:
            # enter context
            self.wind(tymist)  # change tymist and dependencies
            self.tock = tock
            tyme = self.tyme

            # recur context after first yield
            tyme = (yield (tock))

            while (not self.client.connected):
                logger.info("%s:\n waiting for connection to remote %s.\n\n",
                            self.hab.pre, self.client.ha)
                tyme = (yield (self.tock))

            logger.info("%s:\n connected to %s.\n\n", self.hab.pre, self.client.ha)
            tyme = (yield (self.tock))

        except GeneratorExit:  # close context, forced exit due to .close
            pass

        except Exception:  # abort context, forced exit due to uncaught exception
            raise

        finally:  # exit context,  unforced exit due to normal exit of try
            pass

        return True  # return value of yield from, or yield ex.value of StopIteration


def setupDemoController(secrets,  name="who", remotePort=5621, localPort=5620):
    """
    Setup and return doers list to run controller
    """
    secrecies = []
    for secret in secrets:  # convert secrets to secrecies
        secrecies.append([secret])

    # setup habitat
    hab = directing.Habitat(name=name, secrecies=secrecies, temp=True)
    logger.info("\nDirect Mode demo of %s:\nNamed %s on TCP port %s to port %s.\n\n",
                 hab.pre, hab.name, localPort, remotePort)

    # setup doers
    ksDoer = keeping.KeeperDoer(keeper=hab.ks)
    dbDoer = dbing.BaserDoer(baser=hab.db)

    client = clienting.Client(host='127.0.0.1', port=remotePort)
    clientDoer = doing.ClientDoer(client=client)

    if name == 'bob':
        director = BobDirector(hab=hab, client=client, tock=0.125)
    elif name == "sam":
        director = SamDirector(hab=hab, client=client, tock=0.125)
    elif name == 'eve':
        director = EveDirector(hab=hab, client=client, tock=0.125)
    else:
        raise ValueError("Invalid director name={}.".format(name))

    reactor = directing.Reactor(hab=hab, client=client)

    server = serving.Server(host="", port=localPort)
    serverDoer = doing.ServerDoer(server=server)
    directant = directing.Directant(hab=hab, server=server)
    # Reactants created on demand by directant

    return [ksDoer, dbDoer, clientDoer, director, reactor, serverDoer, directant]
