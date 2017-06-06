from CRABClient.UserUtilities import config

SAMPLE = 'SUSYGluGluToBBHToBB_M-500_TuneCUETP8M1_13TeV-pythia8'

config = config()

config.General.workArea      = 'crab_projects_mssmhbb-v1'
config.General.requestName   = SAMPLE
config.General.transferLogs = True


config.JobType.pluginName = 'PrivateMC'
# Name of the CMSSW configuration file
config.JobType.psetName = SAMPLE+'_cfg.py'
config.JobType.numCores = 8

# This string determines the primary dataset of the newly-produced outputs.
# For instance, this dataset will be named /CrabTestSingleMu/something/USER
config.Data.outputPrimaryDataset = SAMPLE
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 1000
config.Data.totalUnits = 1000000
config.Data.publication = True

# This string is used to construct the output dataset name
config.Data.outputDatasetTag = 'PhaseIFall16GS-81X_upgrade2017_realistic_v26-v1'

# Where the output files will be transmitted to
config.Site.storageSite = 'T2_DE_DESY'
config.User.voGroup = 'dcms'

