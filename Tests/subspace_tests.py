# Subspace tests
#
# Written by Konrad Hinsen
# last revision: 2007-3-23
#

import unittest
import MMTK
from MMTK.Proteins import Protein
from MMTK.ForceFields import HarmonicForceField
from MMTK.Subspace import RigidMotionSubspace, PairDistanceSubspace
from MMTK import NormalModes

class PeptideTest(unittest.TestCase):

    """
    Test mode projections on a subspace
    """

    def setUp(self):
        self.universe = MMTK.InfiniteUniverse(HarmonicForceField())
        self.universe.peptide = Protein('bala1')
        self.emodes = NormalModes.EnergeticModes(self.universe)
        self.rm = RigidMotionSubspace(self.universe,
                                      self.universe.peptide.residues())
        self.pd = PairDistanceSubspace(self.universe,
                                       [(self.universe.peptide[0][0].O,
                                         self.universe.peptide[0][-1].CH3)])

    def test_rmProjections(self):
        p = self.rm.projectionOf(self.emodes.rawMode(6)).norm()
        self.assertAlmostEqual(p, 0.9322242598803437)
        p = self.rm.projectionOf(self.emodes.rawMode(7)).norm()
        self.assertAlmostEqual(p, 0.9462254718599316)
        p = self.rm.projectionOf(self.emodes.rawMode(8)).norm()
        self.assertAlmostEqual(p, 0.9267376072638698)
        p = self.rm.projectionOf(self.emodes.rawMode(9)).norm()
        self.assertAlmostEqual(p, 0.9517833097404785)
        p = self.rm.projectionOf(self.emodes.rawMode(10)).norm()
        self.assertAlmostEqual(p, 0.9192284524068041)
        p = self.rm.projectionOf(self.emodes.rawMode(11)).norm()
        self.assertAlmostEqual(p, 0.4950322679744081)
        p = self.rm.projectionOf(self.emodes.rawMode(12)).norm()
        self.assertAlmostEqual(p, 0.9655750904174839)
        p = self.rm.projectionOf(self.emodes.rawMode(13)).norm()
        self.assertAlmostEqual(p, 0.9014696855488994)
        p = self.rm.projectionOf(self.emodes.rawMode(14)).norm()
        self.assertAlmostEqual(p, 0.8697365224866428)
        p = self.rm.projectionOf(self.emodes.rawMode(15)).norm()
        self.assertAlmostEqual(p, 0.7730056445782664)
        p = self.rm.projectionOf(self.emodes.rawMode(16)).norm()
        self.assertAlmostEqual(p, 0.8838199312994008)
        p = self.rm.projectionOf(self.emodes.rawMode(17)).norm()
        self.assertAlmostEqual(p, 0.5737398235455864)
        p = self.rm.projectionOf(self.emodes.rawMode(18)).norm()
        self.assertAlmostEqual(p, 0.7057302370331272)
        p = self.rm.projectionOf(self.emodes.rawMode(19)).norm()
        self.assertAlmostEqual(p, 0.3424214159201944)
        p = self.rm.projectionOf(self.emodes.rawMode(20)).norm()
        self.assertAlmostEqual(p, 0.5885468503837840)
        p = self.rm.projectionOf(self.emodes.rawMode(21)).norm()
        self.assertAlmostEqual(p, 0.4333674301296027)
        p = self.rm.projectionOf(self.emodes.rawMode(22)).norm()
        self.assertAlmostEqual(p, 0.2491254745450491)
        p = self.rm.projectionOf(self.emodes.rawMode(23)).norm()
        self.assertAlmostEqual(p, 0.2119559248130914)
        p = self.rm.projectionOf(self.emodes.rawMode(24)).norm()
        self.assertAlmostEqual(p, 0.4028094188407100)
        p = self.rm.projectionOf(self.emodes.rawMode(25)).norm()
        self.assertAlmostEqual(p, 0.1608763337943279)
        p = self.rm.projectionOf(self.emodes.rawMode(26)).norm()
        self.assertAlmostEqual(p, 0.2060983293242264)
        p = self.rm.projectionOf(self.emodes.rawMode(27)).norm()
        self.assertAlmostEqual(p, 0.3304830568849808)
        p = self.rm.projectionOf(self.emodes.rawMode(28)).norm()
        self.assertAlmostEqual(p, 0.3355232273195539)
        p = self.rm.projectionOf(self.emodes.rawMode(29)).norm()
        self.assertAlmostEqual(p, 0.2450139909420241)
        p = self.rm.projectionOf(self.emodes.rawMode(30)).norm()
        self.assertAlmostEqual(p, 0.1037940415545036)
        p = self.rm.projectionOf(self.emodes.rawMode(31)).norm()
        self.assertAlmostEqual(p, 0.0449058387352367)
        p = self.rm.projectionOf(self.emodes.rawMode(32)).norm()
        self.assertAlmostEqual(p, 0.0818077542082650)
        p = self.rm.projectionOf(self.emodes.rawMode(33)).norm()
        self.assertAlmostEqual(p, 0.1710068451544071)
        p = self.rm.projectionOf(self.emodes.rawMode(34)).norm()
        self.assertAlmostEqual(p, 0.2541211685207877)
        p = self.rm.projectionOf(self.emodes.rawMode(35)).norm()
        self.assertAlmostEqual(p, 0.2231798308970338)
        p = self.rm.projectionOf(self.emodes.rawMode(36)).norm()
        self.assertAlmostEqual(p, 0.1277342580637205)
        p = self.rm.projectionOf(self.emodes.rawMode(37)).norm()
        self.assertAlmostEqual(p, 0.0667396521918318)
        p = self.rm.projectionOf(self.emodes.rawMode(38)).norm()
        self.assertAlmostEqual(p, 0.1590645486036234)
        p = self.rm.projectionOf(self.emodes.rawMode(39)).norm()
        self.assertAlmostEqual(p, 0.3109558405893312)
        p = self.rm.projectionOf(self.emodes.rawMode(40)).norm()
        self.assertAlmostEqual(p, 0.4315424420284669)
        p = self.rm.projectionOf(self.emodes.rawMode(41)).norm()
        self.assertAlmostEqual(p, 0.4361662145295604)
        p = self.rm.projectionOf(self.emodes.rawMode(42)).norm()
        self.assertAlmostEqual(p, 0.2164795646784100)
        p = self.rm.projectionOf(self.emodes.rawMode(43)).norm()
        self.assertAlmostEqual(p, 0.2653371406610991)
        p = self.rm.projectionOf(self.emodes.rawMode(44)).norm()
        self.assertAlmostEqual(p, 0.3719737740169737)
        p = self.rm.projectionOf(self.emodes.rawMode(45)).norm()
        self.assertAlmostEqual(p, 0.4031639430066957)
        p = self.rm.projectionOf(self.emodes.rawMode(46)).norm()
        self.assertAlmostEqual(p, 0.1923409870360145)
        p = self.rm.projectionOf(self.emodes.rawMode(47)).norm()
        self.assertAlmostEqual(p, 0.0837490388595696)
        p = self.rm.projectionOf(self.emodes.rawMode(48)).norm()
        self.assertAlmostEqual(p, 0.1506587981263065)
        p = self.rm.projectionOf(self.emodes.rawMode(49)).norm()
        self.assertAlmostEqual(p, 0.1541813230053046)
        p = self.rm.projectionOf(self.emodes.rawMode(50)).norm()
        self.assertAlmostEqual(p, 0.1253852457937046)
        p = self.rm.projectionOf(self.emodes.rawMode(51)).norm()
        self.assertAlmostEqual(p, 0.0451519999446156)
        p = self.rm.projectionOf(self.emodes.rawMode(52)).norm()
        self.assertAlmostEqual(p, 0.0459616161764973)
        p = self.rm.projectionOf(self.emodes.rawMode(53)).norm()
        self.assertAlmostEqual(p, 0.0089199752625585)
        p = self.rm.projectionOf(self.emodes.rawMode(54)).norm()
        self.assertAlmostEqual(p, 0.0171976043311059)
        p = self.rm.projectionOf(self.emodes.rawMode(55)).norm()
        self.assertAlmostEqual(p, 0.0607892829300145)
        p = self.rm.projectionOf(self.emodes.rawMode(56)).norm()
        self.assertAlmostEqual(p, 0.0346108991769874)
        p = self.rm.projectionOf(self.emodes.rawMode(57)).norm()
        self.assertAlmostEqual(p, 0.0560042266977706)
        p = self.rm.projectionOf(self.emodes.rawMode(58)).norm()
        self.assertAlmostEqual(p, 0.0333007411302587)
        p = self.rm.projectionOf(self.emodes.rawMode(59)).norm()
        self.assertAlmostEqual(p, 0.0589746415638412)
        p = self.rm.projectionOf(self.emodes.rawMode(60)).norm()
        self.assertAlmostEqual(p, 0.0662164228154263)
        p = self.rm.projectionOf(self.emodes.rawMode(61)).norm()
        self.assertAlmostEqual(p, 0.0569476398662924)
        p = self.rm.projectionOf(self.emodes.rawMode(62)).norm()
        self.assertAlmostEqual(p, 0.1614306321754193)
        p = self.rm.projectionOf(self.emodes.rawMode(63)).norm()
        self.assertAlmostEqual(p, 0.1723541658844633)
        p = self.rm.projectionOf(self.emodes.rawMode(64)).norm()
        self.assertAlmostEqual(p, 0.2389830288682290)
        p = self.rm.projectionOf(self.emodes.rawMode(65)).norm()
        self.assertAlmostEqual(p, 0.2413810182829330)

    def test_pdProjections(self):
        p = self.pd.projectionOf(self.emodes.rawMode(6)).norm()
        self.assertAlmostEqual(p, 0.0259939009038073)
        p = self.pd.projectionOf(self.emodes.rawMode(7)).norm()
        self.assertAlmostEqual(p, 0.0047876514809600)
        p = self.pd.projectionOf(self.emodes.rawMode(8)).norm()
        self.assertAlmostEqual(p, 0.1615591757100766)
        p = self.pd.projectionOf(self.emodes.rawMode(9)).norm()
        self.assertAlmostEqual(p, 0.2405264899084614)
        p = self.pd.projectionOf(self.emodes.rawMode(10)).norm()
        self.assertAlmostEqual(p, 0.3907264583491051)
        p = self.pd.projectionOf(self.emodes.rawMode(11)).norm()
        self.assertAlmostEqual(p, 0.1882901477389519)
        p = self.pd.projectionOf(self.emodes.rawMode(12)).norm()
        self.assertAlmostEqual(p, 0.0955950259188246)
        p = self.pd.projectionOf(self.emodes.rawMode(13)).norm()
        self.assertAlmostEqual(p, 0.1691816380626806)
        p = self.pd.projectionOf(self.emodes.rawMode(14)).norm()
        self.assertAlmostEqual(p, 0.1269834888363957)
        p = self.pd.projectionOf(self.emodes.rawMode(15)).norm()
        self.assertAlmostEqual(p, 0.0585510019750427)
        p = self.pd.projectionOf(self.emodes.rawMode(16)).norm()
        self.assertAlmostEqual(p, 0.1987155727131308)
        p = self.pd.projectionOf(self.emodes.rawMode(17)).norm()
        self.assertAlmostEqual(p, 0.0416202640435055)
        p = self.pd.projectionOf(self.emodes.rawMode(18)).norm()
        self.assertAlmostEqual(p, 0.0083368709186168)
        p = self.pd.projectionOf(self.emodes.rawMode(19)).norm()
        self.assertAlmostEqual(p, 0.0747963269729944)
        p = self.pd.projectionOf(self.emodes.rawMode(20)).norm()
        self.assertAlmostEqual(p, 0.1166467937882000)
        p = self.pd.projectionOf(self.emodes.rawMode(21)).norm()
        self.assertAlmostEqual(p, 0.2735732421199717)
        p = self.pd.projectionOf(self.emodes.rawMode(22)).norm()
        self.assertAlmostEqual(p, 0.0677997940610910)
        p = self.pd.projectionOf(self.emodes.rawMode(23)).norm()
        self.assertAlmostEqual(p, 0.0132089144276884)
        p = self.pd.projectionOf(self.emodes.rawMode(24)).norm()
        self.assertAlmostEqual(p, 0.0293996534137576)
        p = self.pd.projectionOf(self.emodes.rawMode(25)).norm()
        self.assertAlmostEqual(p, 0.1960262702512339)
        p = self.pd.projectionOf(self.emodes.rawMode(26)).norm()
        self.assertAlmostEqual(p, 0.0193255450596794)
        p = self.pd.projectionOf(self.emodes.rawMode(27)).norm()
        self.assertAlmostEqual(p, 0.0116129065216995)
        p = self.pd.projectionOf(self.emodes.rawMode(28)).norm()
        self.assertAlmostEqual(p, 0.0487119286975586)
        p = self.pd.projectionOf(self.emodes.rawMode(29)).norm()
        self.assertAlmostEqual(p, 0.1139707988723549)
        p = self.pd.projectionOf(self.emodes.rawMode(30)).norm()
        self.assertAlmostEqual(p, 0.0333743736023489)
        p = self.pd.projectionOf(self.emodes.rawMode(31)).norm()
        self.assertAlmostEqual(p, 0.0692321938048616)
        p = self.pd.projectionOf(self.emodes.rawMode(32)).norm()
        self.assertAlmostEqual(p, 0.0426836883460514)
        p = self.pd.projectionOf(self.emodes.rawMode(33)).norm()
        self.assertAlmostEqual(p, 0.0136682200853454)
        p = self.pd.projectionOf(self.emodes.rawMode(34)).norm()
        self.assertAlmostEqual(p, 0.0664815434268532)
        p = self.pd.projectionOf(self.emodes.rawMode(35)).norm()
        self.assertAlmostEqual(p, 0.0441955448529111)
        p = self.pd.projectionOf(self.emodes.rawMode(36)).norm()
        self.assertAlmostEqual(p, 0.0438087673382064)
        p = self.pd.projectionOf(self.emodes.rawMode(37)).norm()
        self.assertAlmostEqual(p, 0.1059914656578790)
        p = self.pd.projectionOf(self.emodes.rawMode(38)).norm()
        self.assertAlmostEqual(p, 0.0365845154108450)
        p = self.pd.projectionOf(self.emodes.rawMode(39)).norm()
        self.assertAlmostEqual(p, 0.0998395159852196)
        p = self.pd.projectionOf(self.emodes.rawMode(40)).norm()
        self.assertAlmostEqual(p, 0.2147889685217083)
        p = self.pd.projectionOf(self.emodes.rawMode(41)).norm()
        self.assertAlmostEqual(p, 0.0027932725443051)
        p = self.pd.projectionOf(self.emodes.rawMode(42)).norm()
        self.assertAlmostEqual(p, 0.0446508106000885)
        p = self.pd.projectionOf(self.emodes.rawMode(43)).norm()
        self.assertAlmostEqual(p, 0.0308977780411233)
        p = self.pd.projectionOf(self.emodes.rawMode(44)).norm()
        self.assertAlmostEqual(p, 0.1855142969871962)
        p = self.pd.projectionOf(self.emodes.rawMode(45)).norm()
        self.assertAlmostEqual(p, 0.0381180153622493)
        p = self.pd.projectionOf(self.emodes.rawMode(46)).norm()
        self.assertAlmostEqual(p, 0.0445110006376468)
        p = self.pd.projectionOf(self.emodes.rawMode(47)).norm()
        self.assertAlmostEqual(p, 0.0190803177677954)
        p = self.pd.projectionOf(self.emodes.rawMode(48)).norm()
        self.assertAlmostEqual(p, 0.1065088781690438)
        p = self.pd.projectionOf(self.emodes.rawMode(49)).norm()
        self.assertAlmostEqual(p, 0.1822839338518746)
        p = self.pd.projectionOf(self.emodes.rawMode(50)).norm()
        self.assertAlmostEqual(p, 0.2226853432193825)
        p = self.pd.projectionOf(self.emodes.rawMode(51)).norm()
        self.assertAlmostEqual(p, 0.2080892334366243)
        p = self.pd.projectionOf(self.emodes.rawMode(52)).norm()
        self.assertAlmostEqual(p, 0.1617260417722393)
        p = self.pd.projectionOf(self.emodes.rawMode(53)).norm()
        self.assertAlmostEqual(p, 0.2977703889077609)
        p = self.pd.projectionOf(self.emodes.rawMode(54)).norm()
        self.assertAlmostEqual(p, 0.0081060945518584)
        p = self.pd.projectionOf(self.emodes.rawMode(55)).norm()
        self.assertAlmostEqual(p, 0.0263995567579713)
        p = self.pd.projectionOf(self.emodes.rawMode(56)).norm()
        self.assertAlmostEqual(p, 0.0054019046687479)
        p = self.pd.projectionOf(self.emodes.rawMode(57)).norm()
        self.assertAlmostEqual(p, 0.0037053979722240)
        p = self.pd.projectionOf(self.emodes.rawMode(58)).norm()
        self.assertAlmostEqual(p, 0.0620201461976914)
        p = self.pd.projectionOf(self.emodes.rawMode(59)).norm()
        self.assertAlmostEqual(p, 0.0492499453947460)
        p = self.pd.projectionOf(self.emodes.rawMode(60)).norm()
        self.assertAlmostEqual(p, 0.1993635772787671)
        p = self.pd.projectionOf(self.emodes.rawMode(61)).norm()
        self.assertAlmostEqual(p, 0.1482157848692139)
        p = self.pd.projectionOf(self.emodes.rawMode(62)).norm()
        self.assertAlmostEqual(p, 0.1427659988799888)
        p = self.pd.projectionOf(self.emodes.rawMode(63)).norm()
        self.assertAlmostEqual(p, 0.0799913173026774)
        p = self.pd.projectionOf(self.emodes.rawMode(64)).norm()
        self.assertAlmostEqual(p, 0.0215282525475348)
        p = self.pd.projectionOf(self.emodes.rawMode(65)).norm()
        self.assertAlmostEqual(p, 0.0165876082599689)

if __name__ == '__main__':
    unittest.main()