# master config file for FlatTupleGenerator 
# define PSets for various settings and selection cuts
# -- S. Shalhout June 18, 2015

import FWCore.ParameterSet.Config as cms
from DavisRunIITauTau.TupleConfigurations.and_string_concatonator import and_string_concatonator


# individual object cuts used to build the PSets 
# each line appended will be concatenated (using &&) into a single cut string

# electron in EleTau final state :
ele_EleTau = []
ele_EleTau.append("pt>23")
ele_EleTau.append("abs(eta)<2.1")
ele_EleTau.append("abs(dxy)<0.045")
ele_EleTau.append("abs(dz)<0.2")
ele_EleTau.append("passFail_electronMVA80==1.0")
#ele_EleTau.append("relativeIsol('DeltaBetaCorrectedRelIso')<0.1")


# electron in EleMuon final state :
ele_EleMuon = []
ele_EleMuon.append("pt>13")
ele_EleMuon.append("abs(eta)<2.5")
ele_EleMuon.append("abs(dxy)<0.045")
ele_EleMuon.append("abs(dz)<0.2")
ele_EleMuon.append("passFail_electronMVA80==1.0")
#ele_EleMuon.append("relativeIsol('DeltaBetaCorrectedRelIso')<0.15")


# muon in MuonTau final state :
muon_MuonTau = []
muon_MuonTau.append("pt>18")
muon_MuonTau.append("abs(eta)<2.1")
muon_MuonTau.append("abs(dxy)<0.045")
muon_MuonTau.append("abs(dz)<0.2")
muon_MuonTau.append("passesMediumMuonId==1.0")
#muon_MuonTau.append("relativeIsol('DeltaBetaCorrectedRelIso')<0.1")


# muon in EleMuon final state :
muon_EleMuon = []
muon_EleMuon.append("pt>9")
muon_EleMuon.append("abs(eta)<2.4")
muon_EleMuon.append("abs(dxy)<0.045")
muon_EleMuon.append("abs(dz)<0.2")
muon_EleMuon.append("passesMediumMuonId==1.0")
#muon_EleMuon.append("relativeIsol('DeltaBetaCorrectedRelIso')<0.15")




# tau in MuonTau final state :
tau_MuonTau = []
tau_MuonTau.append("pt>20")
tau_MuonTau.append("abs(eta)<2.3")
tau_MuonTau.append("tauID('decayModeFindingNewDMs') > 0.5")                                        
tau_MuonTau.append("abs(dz)<0.2")
tau_MuonTau.append("abs(dzTauVertex)==0.0")


# tau in TauTau final state :
tau_TauTau = []
tau_TauTau.append("pt>45")
tau_TauTau.append("abs(eta)<2.1")
tau_TauTau.append("tauID('decayModeFindingNewDMs') > 0.5")                                        
tau_TauTau.append("abs(dz)<0.2")
tau_TauTau.append("abs(dzTauVertex)==0.0")


# tau in EleTau final state :
tau_EleTau = []
tau_EleTau.append("pt>20")
tau_EleTau.append("abs(eta)<2.3")
tau_EleTau.append("tauID('decayModeFindingNewDMs') > 0.5")                                        
tau_EleTau.append("abs(dz)<0.2")
tau_EleTau.append("abs(dzTauVertex)==0.0")




cut_ele_EleTau = cms.string(and_string_concatonator(ele_EleTau))
cut_ele_EleMuon = cms.string(and_string_concatonator(ele_EleMuon))
cut_muon_MuonTau = cms.string(and_string_concatonator(muon_MuonTau))
cut_muon_EleMuon = cms.string(and_string_concatonator(muon_EleMuon))
cut_tau_TauTau = cms.string(and_string_concatonator(tau_TauTau))
cut_tau_EleTau = cms.string(and_string_concatonator(tau_EleTau))
cut_tau_MuonTau = cms.string(and_string_concatonator(tau_MuonTau))




# VPSet containing selections for different final states, if PSet is not
# provided for a given final state the 
# the events will omitted

# main cut vector PSet :
theCuts = cms.VPSet(

		cms.PSet(   candidatePairType = cms.string("EleTau"),
					electronID = cut_ele_EleTau,
					tauID = cut_tau_EleTau
				),
		cms.PSet(   candidatePairType = cms.string("EleMuon"),
					electronID = cut_ele_EleMuon,
					muonID = cut_muon_EleMuon
				),
		cms.PSet(   candidatePairType = cms.string("MuonTau"),
					muonID = cut_muon_MuonTau,
					tauID = cut_tau_MuonTau
				),
		cms.PSet(   candidatePairType = cms.string("TauTau"),
					tauID = cut_tau_TauTau

				)
	)



		

# config for basic settings 
generalConfig = cms.PSet(

			Mt = cms.vdouble(-1.0e30,30.0), # not used at the moment
			keepOS = cms.bool(True),
			keepSS = cms.bool(True),
			keepTauEsNominal = cms.bool(True),
			keepTauEsUp = cms.bool(False),
			keepTauEsDown = cms.bool(False),

			# how to rank pairs within this selection
			rankByPtSum = cms.bool(True),
			rankByIsolation = cms.bool(False),
			electronIsolationForRank = cms.string("DeltaBetaCorrectedRelIso"),
			muonIsolationForRank = cms.string("DeltaBetaCorrectedRelIso"),
			tauIDisolationForRank = cms.string("byCombinedIsolationDeltaBetaCorrRaw3Hits"),

			# isolations to keep as the leg1_relativeIsolation and 
			# leg2_relativeIsolation branches 

			electronIsolationForRelIsoBranch = cms.string("DeltaBetaCorrectedRelIso"),
			muonIsolationForRelIsoBranch= cms.string("DeltaBetaCorrectedRelIso"),
			tauIsolationForRelIsoBranch = cms.string("byCombinedIsolationDeltaBetaCorrRaw3Hits"),

			# isolations to keep as the veto_relativeIsolation  
			# branches 

			vetoElectronIsolationForRelIsoBranch = cms.string("DeltaBetaCorrectedRelIso"),
			vetoMuonIsolationForRelIsoBranch= cms.string("DeltaBetaCorrectedRelIso"),

			# check isLeg1GoodForHLTPath_Labels, isLeg2GoodForHLTPath_Labels
			# for the following trigger paths (only a summary, need more functions to access new triggers)
			# not requested in FlatTupleConfif_cfi.py summary variables
			# note : the hardcoded THE_MAX variable in FlatTupleGenerator.cc limits the 
			# number of these that we can keep 


			triggerSummaryChecks = cms.vstring(
				"HLT_DoubleMediumIsoPFTau40_Trk1_eta2p1_Reg_v1",
				"HLT_Ele22_eta2p1_WP75_Gsf_LooseIsoPFTau20_v1",
				"HLT_Ele32_eta2p1_WP75_Gsf_v1",
				"HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v1",
				"HLT_IsoMu24_eta2p1_v1",
				"HLT_IsoMu27_v1",
				"HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v1",
				"HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v1"),


			# the Tau IDs we would like to keep in the FlatTuple
			# note : the hardcoded THE_MAX variable in FlatTupleGenerator.cc limits the 
			# number of these that we can keep 

			tauIDsToKeep = cms.vstring(
				"againstElectronLooseMVA5",
				"againstElectronMediumMVA5",
				"againstElectronTightMVA5",
				"againstElectronVLooseMVA5",
				"againstElectronVTightMVA5",
				"againstMuonLoose3",
				"againstMuonTight3",
				"byCombinedIsolationDeltaBetaCorrRaw3Hits",
				"byIsolationMVA3newDMwoLTraw",
				"byIsolationMVA3oldDMwoLTraw",
				"byIsolationMVA3newDMwLTraw",
				"byIsolationMVA3oldDMwLTraw",
				"chargedIsoPtSum",
				#"decayModeFindingOldDMs",
				"neutralIsoPtSum",
				"puCorrPtSum",	
				"decayModeFindingNewDMs"),

			###################
			# jet & bjet ID cut strings
			jetLeptonDRmin = cms.double(0.5),
			# note PU jet ID is not to be applied yet
			#jetIDcut = cms.string("pt>20 && abs(eta) < 4.7 && PU_jetIdPassed && PF_jetIdPassed"),
			#BjetIDcut = cms.string("pt>20 && abs(eta) < 2.4 && PU_jetIdPassed && PF_jetIdPassed && defaultBtagAlgorithm_isPassed")
			jetIDcut = cms.string("pt>20 && abs(eta) < 4.7  && PF_jetIdPassed"),
			BjetIDcut = cms.string("pt>20 && abs(eta) < 2.4 && PF_jetIdPassed && defaultBtagAlgorithm_isPassed")

					)


