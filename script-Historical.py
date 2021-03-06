from Common.Comparators.Index.IndexComparator import IndexComparator
from Common.Plotters.HistoricalPlotter import HistoricalPlotter
from Common.StockMarketIndex.AbstractStockMarketIndex import AbstractStockMarketIndex
from Common.StockMarketIndex.Yahoo.CrudeOilIndex import CrudeOilIndex
from Common.StockMarketIndex.Yahoo.DowJonesIndex import DowJonesIndex
from Common.StockMarketIndex.Yahoo.GoldIndex import GoldIndex
from Common.StockMarketIndex.Yahoo.SilverIndex import SilverIndex
from Common.StockMarketIndex.Yahoo.NasdaqIndex import NasdaqIndex
from Common.StockMarketIndex.Yahoo.NyseComposite import NyseIndex
from Common.StockMarketIndex.Yahoo.SnPTSXComposite import SnPTSXComposite
from Common.StockMarketIndex.Yahoo.FvxIndex import FvxIndex
from Common.StockMarketIndex.Yahoo.SoxIndex import SoxIndex
from Common.StockMarketIndex.Yahoo.TnxIndex import TnxIndex
from Common.StockMarketIndex.Yahoo.TreasuryBill13Index import TreasuryBill13Index
from Common.StockMarketIndex.Yahoo.SnP500Index import SnP500Index
from Common.StockMarketIndex.Yahoo.TyxIndex import TyxIndex
from Common.StockMarketIndex.Yahoo.VixIndex import VixIndex
from Common.StockMarketIndex.Yahoo.Wilshire5kIndex import Wilshire5kIndex
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from Common.StockMarketIndex.Yahoo.DaxIndex import DaxIndex
from Common.StockMarketIndex.Yahoo.Estx50Index import Estx50Index
from Common.StockMarketIndex.Yahoo.EuroNext100Index import EuroNext100Index
from Common.StockMarketIndex.Yahoo.OvxIndex import OvxIndex
from Common.StockMarketIndex.Yahoo.HangSengIndex import HangSengIndex
from Common.StockMarketIndex.Yahoo.BovespaIndex import BovespaIndex
from Common.StockMarketIndex.Yahoo.IpcMexicoIndex import IpcMexicoIndex
from Common.StockMarketIndex.Yahoo.IpsaIndex import IpsaIndex
from Common.StockMarketIndex.Yahoo.JkseIndex import JkseIndex
from Common.StockMarketIndex.Yahoo.KospIndex import KospIndex
from Common.StockMarketIndex.Yahoo.MoexRussiaIndex import MoexRussiaIndex
from Common.StockMarketIndex.Yahoo.Nikkei225Index import Nikkei225Index
from Common.StockMarketIndex.Yahoo.ShenzhenComponentIndex import ShenzhenComponentIndex
from Common.StockMarketIndex.Yahoo.NseIndex import NseIndex
#from Common.StockMarketIndex.Yahoo.Vix3mIndex import Vix3mIndex
from Common.Strategies.TechIndicators.AbstractTechStrategy import AbstractTechStrategy
from Common.Strategies.TechIndicators.EmaStrategy import EmaStrategy
from Common.Strategies.TechIndicators.MacdStrategy import MacdStrategy
from Common.Strategies.TechIndicators.RsiStrategy import RsiStrategy
from Common.Strategies.TechIndicators.SmaStrategy import SmaStrategy
from Common.TechIndicators.AbstractTechIndicator import AbstractTechIndicator
from Common.TechIndicators.EmaIndicator import EmaIndicator
from Common.TechIndicators.MacdIndicator import MacdIndicator
from Common.TechIndicators.RsiIndicator import RsiIndicator
from Common.TechIndicators.SmaIndicator import SmaIndicator

yahooStockOption: YahooStockOption = YahooStockOption('INTC')#'ESTC')XWEB DDOG BEKE GBTC GNDP.V IHI
# DividendYield [2%, 4%] 2.5 - 6
# DividendGrowthRate 6% +
# PEratio [15, 20]
# PBratio [1, 3]
# Return on equity
# Earnings Per Share
# Earnings Per Share Growth
# EBITDA
# Dividend Payout Ratio
# Free Cash flow
# BUFFET AAPLx47.8% BACx10.6% KOx8.6% AXPx6.6% KHCx4.3% CHTRx1.4% DVAx1.4%
#YCBD GRWG FSZ AMZN WELL WCN WMT MWK CP COST KO AMT MA AMD BAC NVDA
#KL WCN OTEX AQN TFII CP CNI LMT RY BRK-B GNW OTEX BPY LMT STOR GME SNE HD
#BCE, ZWB, CM, KEY, VNR, ENB, PPL, SJR.B, NPI, AQN FTS NPI
#ETFs:ARKK TEC.TO, VFV and ACES XEI ARKF QQC-f ZQQ XIT HQU SOXL HZU JNUG FIE BRTXQ
#CCA CGO RCI.B
#DLR VZ ABBV JPM STOR
# Canadian Dividend Aristocrat List from SnP Global
# Canadian Dividend All-Star List
# David Fish's CCC List
# growth portfolio= ETFs & blue chips
# income portfolio= Tx34 IBMx8 ABBVx12 GMx30 Fx126 IRMx30 MPWx60 AGNCx57 PSECx149 MAINx27
# ETSY ESTC VYM - VGT - VTI - VPU / ARKK ARKG ARKQ ARKW
# BND-- <= VXUS- <= BNDX-- <= VNQ- <= VBK <= VYM <= VPU <= VOT ~ VTI <= VIG <= MGK ~ VOO ~ VOOG
# VYM VTSAX/ SWTSX/ FZROX index vs. VTI/ SCHB ETF, VFIAX/ SWPPX/ VXAIX index vs. VOO/ SCHX
# FZROX/ VTSAX FZILX/ VTI FSRNX/ VNQ
# [NFLX, NKE, AMZN] [MRNA, MSFT, CAT] [T, XOM, MO]
# 60% StockMarketFund (FZROX~SWTSX~VTSAX) 20% InternationalFund (FZILX~SWISX~VTIAX) 20% REITFund (FSRNX)
# Sector ETFs: VGT VPU VDC VYM
# Sector Int'l: T (55*30.21$) IBM (14*126.66$) ABBV (21*82.79$) GM (46*35.24$) F (186*8.78$)
# IRM (52*33.48$) MPW (93*17.34$) AGNC (93*17.17$) PSEC (245*6.67$) MAIN (41*37.95$) VYMI (5*59.21$)
# MWK YCBD GRWG FSZ AMZN CGO RCI PPL SJR.B AQN CP CNI TD KL WCN BPY OTEX
# BCE ZWB CM KEY VNR ENB TFII LMT WMT RY BRKB GNW IT
# ETFs: BRTXQ FZILX FSRNX VTSAX FPE HPI
# TFII LSPD T FTS RY SHOP
# AAPL+3 ABBV+ AAOI ADBE+3 ABR+ ABT++ ABX.TO&GOLD ACES ADC+ ADP AGNC AKAM AMGN AMD+20 AMP AMT+ AMZN+3 ANTM+ AQN+ AQN.TO+
# ARKK+++ ARKF++ ARKG+ ARKQ ARKW++++ APPS+++ APPN+5 AVGO++ AA. APHA+ ASAN ARKF ARKK AVAV AVGO++ AVB AYX++ AZN AWK+ ANET+
# AEM+ AEM.TO+ AT.TO ATZ.TO. ACO-X.TO+ ARKG+ A++ ACO-X.TO! ACN++ AIVSX+ AMC. ATVI+1.5 AXP+
# BA BCE BCE.TO. BNS BPY BABA++ BIDU- BBBY BNTX BRK-B+ BRTXQ BYND BNS.TO. BIP+ BZUN+ BILI++ BEP+ BYND+ BAM-A.TO+
# BMO.TO. BTI- BMY- BGS. BAND+5
# CAG CAT CCA CCA.TO. CAR.UN.TO CGNX CGO CGO.TO. CHD CHWY CL. CLX+ CM CNI CSU.TO CSX CVD CMCSA COST++ CP CSCO+ CDNS+3.5
# CNQ.TO. CSIQ+1.5 CELH+ CM+ CPX.TO++ CVA. CLH+ COLL. COUP+5 CRM+1.5 CHTR+2
# CNR.TO+ CU.TO. CSU.TO++ CTC-A.TO+ CLR.TO. CRWD++ CARR++ CB- CU.TO. CRSP++++++ C. CLNE. CMCSA+ CIBR+
# DCBO.TO DND.TO DLHC DKNG+ DDOG+ DOL.TO+ DND.TO+ DIS+ DHR+++ DTE+ DE++ DOCU+3 DVN. DAL. DLR+ DTE+ DVA.
# EMR+ ENB- ENB.TO- ESS ESTC+ ESPO EMA.TO ET ETSY+10 ENGH.TO+ ENPH+ EEM EQB.TO+ ELY+ ESS- EPD+ EB. ENPH+25 ET. EBAY+
# F FD.TO FF.TO FFMG FENY FIE FIVG FROG FSLR FSLY++ FSRNX FSZ FTS+ FTS.TO+ FOOD.TO FZILX FZROX FVRR FXAIX FEYE. FRT. FCEL.
# FTEC+2 FAST+1.5 FB+1.5
# GE. GD. GM GFI++ GIS GLD+ GLW GMF GNW GRWG GILD GBTC GAMR GSY.TO+ GOOD+ GXC+ GOOG+2 GOOGL+2 GGG++
# HD+ HLT HQU HZU HEO.V HII. HLF.TO. HUBS+3 HRL. HTA. HIW. HACK++
# IBUY IWFH INTC+ INTU+2 IPO+2 IIVI IIPR+++++ INVH+ IVAC IGV+ IBM. IRM+ IT+ IPFF. IWY++ ICLN++
# JKS+2 JD+ JNJ+ JPM+ JNUG. JNPR.
# KEY K KXS.TO KDP KL KL.TO KO! KR KMI. K.TO++ KXS.TO+ KHC.
# LB.TO LMT+ LMND LOW++ LSPD++ LSPD.TO++ LVGO LOGI+ LAND+ LMND+ LMT+ LULU+3 LUV.
# M MA+2 MAIN MELI+10 MFI.TO MO. MU+3 MCD+ MGM MPW MRK+ MARA MRNA MRVL MSFT+2.5 MWK MDY MRU.TO+ MSCI+ NXST MFC.TO. MXIM+
# MDLZ. MDB+6 MAA. MTUM+ NWC.TO. MGNI+
# NEE+ NEM+ NET+2 NKE+ NSP NEAR NFLX+++ NIO+4 NLY. NLOK NNDM NPI NOBL+ NVEI.TO NVDA+5 NOW+4 NRZ-
# O+ OTEX OHI O- NWC.TO. OKTA+++++ OKE++ MC-
# PM- PANW PFE+ PINS PG+ PGX PEP+ PLAN PLTR+1.5 PPL.TO+ PBA+ PBW+3.5 PRU- PVD PTON PAWZ PSEC PYPL+3 PCTY+++ PKI.TO PHO
# PAAS+++ PAYC+6 PBH. PDD+3 PNC+ PTGX+ PIODX+ PKI.TO+ PINS+2 PNR+ PHM++ POW.TO.
# QCOM QQC-f QQQ QRVO QSR.TO+ QQQJ++ QRS.TO
# RBA RCI+ RCI.B.TO+ REAL.TO RCL.S REGI ROK+ RUN RY+ RY.TO+ RIOT RHS RNG+9 ROKU+ RF+ RNW.TO++ ROP+ RSG++ RTX.
# SU. SU.TO. SIS.TO+ SNA SBUX+ SHOP+20 SHOP.TO+20 SPLK SPYD SJR.B SJR-B.TO SLV+ SNAP SNOW+ SPOT SOXL SRU.UN.TO. SPG SAP
# SPNS+2 SNPS+3 STOR+ STAG SEDG+ SJR-B.TO SOY.TO. SYK++ STX+ SQ+8 SFTBY+2 SAVA. SMOG+2 SE+7.5 SCHA+
# T+ T.TO+ TD TTD+15 TDOC+7.5 TEC.TO TAL+ TEAM+5 TFII+ TFII.TO+ TGT- TRMB TSLA+++ TRP TRP.TO TTD+15 TOU.TO TROW TWLO+6 TWST+
# TVE.TO. TPB+++ TPR. TSN- TSM+ TCOM. TXN+2 TTCF+2
# U UNM UNP UPWK UNM- UDN.
# VDC VFC VFF VFV.TO VG+1.5 VGT++ VMW VNR VPL VPU VTSAX VYM VYMI VZ+ V+1.5 VOO+ VOOG+ VNQ+ VIOO VHT VSP.TO VEQT.TO+
# VGRO.TO+ VEEV+6 VTV+
# W+3 WCN++ WCN.TO++ WELL.TO WEED.TO++ WFG WM++ WMT++ WORK. WPC.
# XEI.TO. XIT XBC.TO XOM. XWEB+ XLK+ XBC.V+++ XTC.TO. ZS++
# YCBD.
# ZG+3.5 ZM+3 ZQQ.TO+1.5 ZS+3 ZWB.TO. ZUO. ZTS+2
# AYX+4 PLAN+1.5 ASAN+ DDOG+1.5 DT+ FOUR++ FROG. MDLA+ NTNX. PEGA+3 PSTG+ SMAR++ WDAY++
print(yahooStockOption.DataFrame.describe(include='all'))
sAnP500: AbstractStockMarketIndex = SnP500Index('yahoo', "^GSPC", yahooStockOption.TimeSpan)
vixIndex: AbstractStockMarketIndex = VixIndex('yahoo', "^VIX", yahooStockOption.TimeSpan)
#''' #ovxIndex: AbstractStockMarketIndex = OvxIndex('yahoo', "^OVX", yahooStockOption.TimeSpan)
sAndPTsx: AbstractStockMarketIndex = SnPTSXComposite('yahoo', "^GSPTSE", yahooStockOption.TimeSpan)
nasdaqIndex: AbstractStockMarketIndex = NasdaqIndex('yahoo', "^IXIC", yahooStockOption.TimeSpan)
nyseIndex: AbstractStockMarketIndex = NyseIndex('yahoo', "^NYA", yahooStockOption.TimeSpan)
dowJonesIndex: AbstractStockMarketIndex = DowJonesIndex('yahoo', "^DJI", yahooStockOption.TimeSpan)
goldIndex: AbstractStockMarketIndex = GoldIndex('yahoo', "GC=F", yahooStockOption.TimeSpan)
silverIndex: AbstractStockMarketIndex = SilverIndex('yahoo', "SI=F", yahooStockOption.TimeSpan)
crudeOilIndex: AbstractStockMarketIndex = CrudeOilIndex('yahoo', "CL=F", yahooStockOption.TimeSpan)
soxIndex: AbstractStockMarketIndex = SoxIndex('yahoo', "^SOX", yahooStockOption.TimeSpan)
tnxIndex: AbstractStockMarketIndex = TnxIndex('yahoo', "^TNX", yahooStockOption.TimeSpan)
tyxIndex: AbstractStockMarketIndex = TyxIndex('yahoo', "^TYX", yahooStockOption.TimeSpan)
fvxIndex: AbstractStockMarketIndex = FvxIndex('yahoo', "^FVX", yahooStockOption.TimeSpan)
irxIndex: AbstractStockMarketIndex = TreasuryBill13Index('yahoo', "^IRX", yahooStockOption.TimeSpan)
wilshire5kIndex: AbstractStockMarketIndex = Wilshire5kIndex('yahoo', "^W5000", yahooStockOption.TimeSpan)
#vix3mIndex: AbstractStockMarketIndex = Vix3mIndex('yahoo', "^VIX3M", yahooStockOption.TimeSpan)
#euroNext100Index: AbstractStockMarketIndex = EuroNext100Index('yahoo', "^N100", yahooStockOption.TimeSpan)
#estx50Index: AbstractStockMarketIndex = Estx50Index('yahoo', "^N100", yahooStockOption.TimeSpan)
#daxIndex: AbstractStockMarketIndex = DaxIndex('yahoo', "^GDAXI", yahooStockOption.TimeSpan)
#nikkei225Index: AbstractStockMarketIndex = Nikkei225Index('yahoo', "^N225", yahooStockOption.TimeSpan)
#moexRussiaIndex: AbstractStockMarketIndex = MoexRussiaIndex('yahoo', "IMOEX.ME", yahooStockOption.TimeSpan)
#hangSengIndex: AbstractStockMarketIndex = HangSengIndex('yahoo', "^HSI", yahooStockOption.TimeSpan)
#shenzhenComponentIndex: AbstractStockMarketIndex = ShenzhenComponentIndex('yahoo', "399001.SZ", yahooStockOption.TimeSpan)
#nifty50Index: AbstractStockMarketIndex = NseIndex('yahoo', "^NSEI", yahooStockOption.TimeSpan)
#bovespaIndex: AbstractStockMarketIndex = BovespaIndex('yahoo', "^BVSP", yahooStockOption.TimeSpan)
#ipcMexicoIndex: AbstractStockMarketIndex = IpcMexicoIndex('yahoo', "^MXX", yahooStockOption.TimeSpan)
#ipsaIndex: AbstractStockMarketIndex = IpsaIndex('yahoo', "^IPSA", yahooStockOption.TimeSpan)
#jkseIndex: AbstractStockMarketIndex = JkseIndex('yahoo', "^JKSE", yahooStockOption.TimeSpan)
#kospIndex: AbstractStockMarketIndex = KospIndex('yahoo', "^KS11", yahooStockOption.TimeSpan)
marketIndices = list()
marketIndices.append(sAnP500)
marketIndices.append(vixIndex)
#marketIndices.append(ovxIndex)
marketIndices.append(sAndPTsx)
marketIndices.append(nasdaqIndex)
marketIndices.append(nyseIndex)
marketIndices.append(dowJonesIndex)
marketIndices.append(goldIndex)
marketIndices.append(silverIndex)
marketIndices.append(crudeOilIndex)
marketIndices.append(soxIndex)
marketIndices.append(tnxIndex)
marketIndices.append(tyxIndex)
marketIndices.append(irxIndex)
marketIndices.append(fvxIndex)
marketIndices.append(wilshire5kIndex)
#marketIndices.append(vix3mIndex)
#marketIndices.append(euroNext100Index)
#marketIndices.append(estx50Index)
#marketIndices.append(daxIndex)
#marketIndices.append(nikkei225Index)
#marketIndices.append(moexRussiaIndex)
#marketIndices.append(hangSengIndex)
#marketIndices.append(shenzhenComponentIndex)
#marketIndices.append(nifty50Index)
#marketIndices.append(bovespaIndex)
#marketIndices.append(ipcMexicoIndex)
#marketIndices.append(ipsaIndex)
#marketIndices.append(jkseIndex)
#marketIndices.append(kospIndex)
indexComparator: IndexComparator = IndexComparator(yahooStockOption, marketIndices)
#'''
yahooStockOptionPlotter: HistoricalPlotter = HistoricalPlotter(yahooStockOption, vixIndex, sAnP500)
#yahooStockOptionPlotter.SnP500Plot().show()
yahooStockOptionPlotter.GraphPlot().show()
yahooStockOptionPlotter.Plot().show()
#yahooStockOptionPlotter.PlotTimely()
#exit(31415)
#yahooMacdIndicator: MacdIndicator = yahooStockOptionPlotter.MacdInd #MacdIndicator(yahooStockOption)
print(yahooStockOptionPlotter.MacdInd.GetData().columns)
#yahooMacdIndicator.PlotData().show()
#yahooMacdStrategy: MacdStrategy = yahooStockOptionPlotter.MacdStrat #MacdStrategy(yahooMacdIndicator)
#yahooStockOptionPlotter.MacdStrat.Plot().show()
yahooStockOptionPlotter.MacdStrat.PlotAll().show()
#yahooSmaIndicator: SmaIndicator = yahooStockOptionPlotter.SmaInd #SmaIndicator(yahooStockOption)
print(yahooStockOptionPlotter.SmaInd.GetData().columns)
#yahooSmaIndicator.PlotData().show()
#yahooSmaStrategy: SmaStrategy = yahooStockOptionPlotter.SmaStrat #SmaStrategy(yahooSmaIndicator)
#yahooStockOptionPlotter.SmaStrat.Plot().show()
yahooStockOptionPlotter.SmaStrat.PlotAll().show()
#yahooEmaIndicator: EmaIndicator = yahooStockOptionPlotter.EmaInd #EmaIndicator(yahooStockOption)
print(yahooStockOptionPlotter.EmaInd.GetData().columns)
#yahooEmaIndicator.PlotData().show()
#yahooEmaStrategy: EmaStrategy = yahooStockOptionPlotter.EmaStrat #EmaStrategy(yahooEmaIndicator)
#yahooStockOptionPlotter.EmaStrat.Plot().show()
yahooStockOptionPlotter.EmaStrat.PlotAll().show()
#yahooRsiIndicator: RsiIndicator = yahooStockOptionPlotter.RsiInd #RsiIndicator(yahooStockOption)
print(yahooStockOptionPlotter.RsiInd.GetData().columns)
#yahooStockOptionPlotter.RsiInd.PlotData().show()
#yahooEmaStrategy: RsiStrategy = yahooStockOptionPlotter.RsiStrat #RsiStrategy(yahooEmaIndicator)
yahooStockOptionPlotter.RsiStrat.PlotAll().show()
#***
yahooStockOptionPlotter.IndicatorPlot().show()
yahooStockOptionPlotter.StrategyPlot().show()
# preprocessing
## Mean removal
print('MEAN=', yahooStockOption.Data.Sparse.mean(axis=0))
print('SD=', yahooStockOption.Data.Sparse.std(axis=0))
# classification by classes
# viz
## uni variate
