from Common.Comparators.Index.IndexComparator import IndexComparator
from Common.Plotters.HistoricalPlotter import HistoricalPlotter
from Common.StockMarketIndex.AbstractStockMarketIndex import AbstractStockMarketIndex
from Common.StockMarketIndex.Yahoo.CrudeOilIndex import CrudeOilIndex
from Common.StockMarketIndex.Yahoo.DaxIndex import DaxIndex
from Common.StockMarketIndex.Yahoo.DowJonesIndex import DowJonesIndex
from Common.StockMarketIndex.Yahoo.Estx50Index import Estx50Index
from Common.StockMarketIndex.Yahoo.EuroNext100Index import EuroNext100Index
from Common.StockMarketIndex.Yahoo.GoldIndex import GoldIndex
from Common.StockMarketIndex.Yahoo.OvxIndex import OvxIndex
from Common.StockMarketIndex.Yahoo.SilverIndex import SilverIndex
from Common.StockMarketIndex.Yahoo.HangSengIndex import HangSengIndex
from Common.StockMarketIndex.Yahoo.BovespaIndex import BovespaIndex
from Common.StockMarketIndex.Yahoo.IpcMexicoIndex import IpcMexicoIndex
from Common.StockMarketIndex.Yahoo.IpsaIndex import IpsaIndex
from Common.StockMarketIndex.Yahoo.JkseIndex import JkseIndex
from Common.StockMarketIndex.Yahoo.KospIndex import KospIndex
from Common.StockMarketIndex.Yahoo.MoexRussiaIndex import MoexRussiaIndex
from Common.StockMarketIndex.Yahoo.NasdaqIndex import NasdaqIndex
from Common.StockMarketIndex.Yahoo.Nikkei225Index import Nikkei225Index
from Common.StockMarketIndex.Yahoo.NyseComposite import NyseIndex
from Common.StockMarketIndex.Yahoo.ShenzhenComponentIndex import ShenzhenComponentIndex
from Common.StockMarketIndex.Yahoo.SnPTSXComposite import SnPTSXComposite
from Common.StockMarketIndex.Yahoo.SnP500Index import SnP500Index
from Common.StockMarketIndex.Yahoo.NseIndex import NseIndex
from Common.StockMarketIndex.Yahoo.FvxIndex import FvxIndex
from Common.StockMarketIndex.Yahoo.SoxIndex import SoxIndex
from Common.StockMarketIndex.Yahoo.TreasuryBill13Index import TreasuryBill13Index
#from Common.StockMarketIndex.Yahoo.Vix3mIndex import Vix3mIndex
from Common.StockMarketIndex.Yahoo.VixIndex import VixIndex
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
#from Common.Measures.Time.TimeSpan import TimeSpan

yahooStockOption: YahooStockOption = YahooStockOption('KMI')#'ESTC')XWEB
#YCBD GRWG FSZ AMZN WELL WCN WMT MWK CP COST KO AMT MA AMD BAC NVDA
#KL WCN OTEX AQN TFII CP CNI LMT RY BRK-B GNW OTEX BPY LMT STOR GME SNE HD
#BCE, ZWB, CM, KEY, VNR, ENB, PPL, SJR.B, NPI, AQN FTS NPI
#ETFs:ARKK TEC.TO, VFV and ACES XEI ARKF QQC-f ZQQ XIT HQU SOXL HZU JNUG FIE BRTXQ
#CCA CGO RCI.B
# Canadian Dividend Aristocrat List from SnP Global
# Canadian Dividend All-Star List
# David Fish's CCC List
# growth portfolio= ETFs & blue chips
# income portfolio= Tx34 IBMx8 ABBVx12 GMx30 Fx126 IRMx30 MPWx60 AGNCx57 PSECx149 MAINx27
# ETSY ESTC VYM - VGT - VTI - VPU
# VYM VTSAX/ SWTSX/ FZROX index vs. VTI/ SCHB ETF, VFIAX/ SWPPX/ VXAIX index vs. VOO/ SCHX
# FZROX FZILX FSRNX
# VTSAX
# [NFLX, NKE, AMZN] [MRNA, MSFT, CAT] [T, XOM, MO]
# 60% StockMarketFund (FZROX~SWTSX~VTSAX) 20% InternationalFund (FZILX~SWISX~VTIAX) 20% REITFund (FSRNX)
# Sector ETFs: VGT VPU VDC VYM
# Sector Int'l: T (55*30.21$) IBM (14*126.66$) ABBV (21*82.79$) GM (46*35.24$) F (186*8.78$)
# IRM (52*33.48$) MPW (93*17.34$) AGNC (93*17.17$) PSEC (245*6.67$) MAIN (41*37.95$) VYMI (5*59.21$)
# MWK YCBD GRWG FSZ AMZN CGO RCI PPL SJR.B AQN CP CNI TD KL WCN BPY OTEX
# BCE ZWB CM KEY VNR ENB TFII LMT WMT RY BRKB GNW IT
# ETFs: BRTXQ FZILX FSRNX VTSAX FPE HPI
# TFII LSPD T FTS RY SHOP
# AAPL ABBV AAOI ABR+ ABT ABX.TO&GOLD ACES ADP AGNC AKAM AMGN AMD AMP AMT AMZN ANTM AQN AQN.TO ARKK ARKG ARKQ ARKW
# APHA ASAN ARKF ARKK AVAV AVGO AVB AYX AZN AIVSX+
# BA BCE BNS BPY BABA BBBY BNTX BRK-B BRKA BRKB BRTXQ BYND BNS.TO
# CAG CAT CCA CCA.TO. CAR.UN.TO CGNX CGO CGO.TO. CHD CHWY CL- CLX CM CNI CSU.TO CSX CVD CMCSA COST CP CRM CSCO CDNS CNQ.TO CSIQ
# DCBO.TO DND.TO CU.TO DLHC
# EMR+ ENB ENB.TO ESS ESTC ESPO EMA.TO ET ETSY+
# F FD.TO FF.TO FFMG FENY FIE FIVG FROG FSLR FSLY+ FSRNX FSZ FTS FOOD.TO FZILX FZROX FVRR FXAIX
# GM GIS GLD GLW GMF GNW GRWG GILD GBTC GAMR
# HD HLT HQU HZU HEO.V IBM IBUY IWFH INTC IPO IIVI IVAC IBM IRM+ IT IPFF JKS JNJ+ JPM+ JNUG JNPR
# KEY K KXS.TO KDP KL KL.TO KO- KR KMI K.TO
# LB.TO LMT LMND LOW+ LSPD LVGO
# M MA MAIN MELI MFI.TO MO MU MCD- MGM MPW MRK MARA MRNA MRVL MSFT MWK MDY MRU.TO
# NEE+ NEM+ NET NKE NSP NEAR NFLX NLY NLOK NNDM NPI NVEI.TO O+ OTEX
# PM PANW PFE PINS PGX PEP PLAN PLTR PPL PRU PVD PTON PAWZ PSEC PYPL PKI.TO PIODX+
# QCOM QQC-f QQQ QRVO RBA RCI RCI.B REAL.TO REGI ROK+ RUN RY+ RY.TO+ RCI.B.TO RIOT RHS
# SU SU.TO SNA SBUX SHOP SPLK SPYD SJR.B SJR-B.TO SLV SNAP SNOW SPOT SOXL SRU.UN.TO. SPG SAP SPNS
# T+ TD TDOC TEC.TO TEAM TFII TFII.TO+ TGT- TRMB TSLA TRP&TRP.TO TTD TOU.TO TROW TWLO TXN U UNM UNP UPWK
# VDC VFC VFF VFV VGT VMW VNR VPL VPU VTSAX VYM VYMI VZ V VOO+ VOOG+ VNQ+ VIOO VHT
# WCN WCN.TO+ WELL WFG WMT- WORK XEI XIT XBC.TO XOM XWEB YCBD ZG ZM ZQQ ZS ZWB
print(yahooStockOption.HistoricalData.describe(include='all'))
sAnP500: AbstractStockMarketIndex = SnP500Index('yahoo', "^GSPC", yahooStockOption.TimeSpan)
vixIndex: AbstractStockMarketIndex = VixIndex('yahoo', "^VIX", yahooStockOption.TimeSpan)
'''
ovxIndex: AbstractStockMarketIndex = OvxIndex('yahoo', "^OVX", yahooStockOption.TimeSpan)
sAndPTsx: AbstractStockMarketIndex = SnPTSXComposite('yahoo', "^GSPTSE", yahooStockOption.TimeSpan)
nasdaqIndex: AbstractStockMarketIndex = NasdaqIndex('yahoo', "^IXIC", yahooStockOption.TimeSpan)
nyseIndex: AbstractStockMarketIndex = NyseIndex('yahoo', "^NYA", yahooStockOption.TimeSpan)
dowJonesIndex: AbstractStockMarketIndex = DowJonesIndex('yahoo', "^DJI", yahooStockOption.TimeSpan)
goldIndex: AbstractStockMarketIndex = GoldIndex('yahoo', "GC=F", yahooStockOption.TimeSpan)
silverIndex: AbstractStockMarketIndex = SilverIndex('yahoo', "SI=F", yahooStockOption.TimeSpan)
crudeOilIndex: AbstractStockMarketIndex = CrudeOilIndex('yahoo', "CL=F", yahooStockOption.TimeSpan)
soxIndex: AbstractStockMarketIndex = SoxIndex('yahoo', "^SOX", yahooStockOption.TimeSpan)
#vix3mIndex: AbstractStockMarketIndex = Vix3mIndex('yahoo', "^VIX3M", yahooStockOption.TimeSpan)
daxIndex: AbstractStockMarketIndex = DaxIndex('yahoo', "^GDAXI", yahooStockOption.TimeSpan)
euroNext100Index: AbstractStockMarketIndex = EuroNext100Index('yahoo', "^N100", yahooStockOption.TimeSpan)
estx50Index: AbstractStockMarketIndex = Estx50Index('yahoo', "^N100", yahooStockOption.TimeSpan)
nikkei225Index: AbstractStockMarketIndex = Nikkei225Index('yahoo', "^N225", yahooStockOption.TimeSpan)
moexRussiaIndex: AbstractStockMarketIndex = MoexRussiaIndex('yahoo', "IMOEX.ME", yahooStockOption.TimeSpan)
hangSengIndex: AbstractStockMarketIndex = HangSengIndex('yahoo', "^HSI", yahooStockOption.TimeSpan)
shenzhenComponentIndex: AbstractStockMarketIndex = ShenzhenComponentIndex('yahoo', "399001.SZ", yahooStockOption.TimeSpan)
bovespaIndex: AbstractStockMarketIndex = BovespaIndex('yahoo', "^BVSP", yahooStockOption.TimeSpan)
ipcMexicoIndex: AbstractStockMarketIndex = IpcMexicoIndex('yahoo', "^MXX", yahooStockOption.TimeSpan)
nifty50Index: AbstractStockMarketIndex = NseIndex('yahoo', "^NSEI", yahooStockOption.TimeSpan)
ipsaIndex: AbstractStockMarketIndex = IpsaIndex('yahoo', "^IPSA", yahooStockOption.TimeSpan)
fvxIndex: AbstractStockMarketIndex = FvxIndex('yahoo', "^FVX", yahooStockOption.TimeSpan)
irxIndex: AbstractStockMarketIndex = TreasuryBill13Index('yahoo', "^IRX", yahooStockOption.TimeSpan)
jkseIndex: AbstractStockMarketIndex = JkseIndex('yahoo', "^JKSE", yahooStockOption.TimeSpan)
kospIndex: AbstractStockMarketIndex = KospIndex('yahoo', "^KS11", yahooStockOption.TimeSpan)
marketIndices = list()
marketIndices.append(ovxIndex)
marketIndices.append(vixIndex)
marketIndices.append(sAnP500)
marketIndices.append(sAndPTsx)
marketIndices.append(nasdaqIndex)
marketIndices.append(nyseIndex)
marketIndices.append(dowJonesIndex)
marketIndices.append(goldIndex)
marketIndices.append(silverIndex)
marketIndices.append(crudeOilIndex)
marketIndices.append(soxIndex)
#marketIndices.append(vix3mIndex)
marketIndices.append(daxIndex)
marketIndices.append(euroNext100Index)
marketIndices.append(estx50Index)
marketIndices.append(nikkei225Index)
marketIndices.append(moexRussiaIndex)
marketIndices.append(hangSengIndex)
marketIndices.append(shenzhenComponentIndex)
marketIndices.append(bovespaIndex)
marketIndices.append(ipcMexicoIndex)
marketIndices.append(nifty50Index)
marketIndices.append(ipsaIndex)
marketIndices.append(fvxIndex)
marketIndices.append(irxIndex)
marketIndices.append(jkseIndex)
marketIndices.append(kospIndex)
indexComparator: IndexComparator = IndexComparator(yahooStockOption, marketIndices)
'''
yahooStockOptionPlotter: HistoricalPlotter = HistoricalPlotter(yahooStockOption, vixIndex, sAnP500)
yahooStockOptionPlotter.GraphPlot().show()
yahooStockOptionPlotter.Plot().show()
#exit(31415)
yahooStockOptionPlotter.PlotTimely()
#yahooStockOptionPlotter.Daily().show()
#yahooStockOptionPlotter.DailyCum().show()
#yahooStockOptionPlotter.DailyHist().show()
#yahooStockOptionPlotter._plotDaily().show()
#yahooStockOptionPlotter._plotWeekly().show()
#yahooStockOptionPlotter.Monthly().show()
#yahooStockOptionPlotter.MonthlyCum().show()
#yahooStockOptionPlotter.MonthlyHist().show()
#yahooStockOptionPlotter._plotMonthly().show()
#yahooStockOptionPlotter._plotQuarterly().show()
#yahooStockOptionPlotter._plotAnnually().show()
# preprocessing
## Mean removal
print('MEAN=', yahooStockOption.Data.Sparse.mean(axis=0))
print('SD=', yahooStockOption.Data.Sparse.std(axis=0))
# classification by classes
# viz
## uni variate
