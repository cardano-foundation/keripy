# -*- encoding: utf-8 -*-
"""
tests delegation primaily from keri.core.eventing

"""
import os
import datetime

import pytest

from keri import help
from keri.help import helping
from keri.db import dbing
from keri.base import keeping, directing
from keri.core import coring, eventing


logger = help.ogler.getLogger()


def test_witness():
    """
    Test event validation logic with witnesses

    cam is controller
    van is validator
    wes is a witness
    wok is a witness
    wam is a witness

    """
    salt = coring.Salter(raw=b'abcdef0123456789').qb64

    with dbing.openDB(name="cam") as camDB, keeping.openKS(name="cam") as camKS, \
         dbing.openDB(name="van") as vanDB, keeping.openKS(name="van") as vanKS, \
         dbing.openDB(name="wes") as wesDB, keeping.openKS(name="wes") as wesKS, \
         dbing.openDB(name="wok") as wokDB, keeping.openKS(name="wok") as wokKS, \
         dbing.openDB(name="wam") as wamDB, keeping.openKS(name="wam") as wamKS:

        # witnesses first so can setup inception event for cam
        # setup Wes's habitat nontrans
        # Wes's receipts will be rcts with a receipt couple attached
        sith = '1'  # hex str of threshold int
        wesHab = directing.Habitat(ks=wesKS, db=wesDB, isith=sith, icount=1,
                                   salt=salt, transferable=False, temp=True)  # stem is .name
        assert wesHab.ks == wesKS
        assert wesHab.db == wesDB
        assert not wesHab.kever.prefixer.transferable
        # create non-local kevery for Wes to process nonlocal msgs
        wesKevery = eventing.Kevery(kevers=wesHab.kevers,
                                    db=wesHab.db,
                                    framed=True,
                                    opre=wesHab.pre,
                                    local=False)

        # setup Wok's habitat nontrans
        # Wok's receipts will be rcts with a receipt couple attached
        sith = '1'  # hex str of threshold int
        wokHab = directing.Habitat(ks=wokKS, db=wokDB, isith=sith, icount=1,
                                   salt=salt, transferable=False, temp=True)  # stem is .name
        assert wokHab.ks == wokKS
        assert wokHab.db == wokDB
        assert not wokHab.kever.prefixer.transferable
        # create non-local kevery for Wok to process nonlocal msgs
        wokKevery = eventing.Kevery(kevers=wokHab.kevers,
                                    db=wokHab.db,
                                    framed=True,
                                    opre=wokHab.pre,
                                    local=False)

        # setup Wam's habitat nontrans
        # Wams's receipts will be rcts with a receipt couple attached
        sith = '1'  # hex str of threshold int
        wamHab = directing.Habitat(ks=wamKS, db=wamDB, isith=sith, icount=1,
                                   salt=salt, transferable=False, temp=True)  # stem is .name
        assert wamHab.ks == wamKS
        assert wamHab.db == wamDB
        assert not wamHab.kever.prefixer.transferable
        # create non-local kevery for Wam to process nonlocal msgs
        wamKevery = eventing.Kevery(kevers=wamHab.kevers,
                                    db=wamHab.db,
                                    framed=True,
                                    opre=wamHab.pre,
                                    local=False)

        # setup Cam's habitat trans multisig
        sith = '2'  # hex str of threshold int
        camHab = directing.Habitat(ks=camKS, db=camDB, isith=sith, icount=3,
                                   salt=salt, temp=True)  # stem is .name
        assert camHab.ks == camKS
        assert camHab.db == camDB
        assert camHab.kever.prefixer.transferable

        # create non-local kevery for Cam to process onlocal msgs
        camKevery = eventing.Kevery(kevers=camHab.kevers,
                                    db=camHab.db,
                                    framed=True,
                                    opre=camHab.pre,
                                    local=False)

        # setup Van's habitat trans multisig
        sith = '2'  # two of three signing threshold
        vanHab = directing.Habitat(ks=vanKS, db=vanDB, isith=sith, icount=3,
                                   salt=salt, temp=True)  # stem is .name
        assert vanHab.ks == vanKS
        assert vanHab.db == vanDB
        assert vanHab.kever.prefixer.transferable
        # create non-local kevery for Van to process nonlocal msgs
        vanKevery = eventing.Kevery(kevers=vanHab.kevers,
                                    db=vanHab.db,
                                    framed=True,
                                    opre=vanHab.pre,
                                    local=False)

        camMsgs = bytearray()




    assert not os.path.exists(wokKS.path)
    assert not os.path.exists(wokDB.path)
    assert not os.path.exists(wesKS.path)
    assert not os.path.exists(wesDB.path)
    assert not os.path.exists(vanKS.path)
    assert not os.path.exists(vanDB.path)
    assert not os.path.exists(camKS.path)
    assert not os.path.exists(camDB.path)

    """End Test"""


if __name__ == "__main__":
    test_witness()