import os
import json
import opensmile
import audiofile


def extract_features_opensmile_lld(audio):
    signal, sampling_rate=audiofile.read(audio,always_2d=True)
    silme=opensmile.Smile(
        feature_set=opensmile.FeatureSet.eGeMAPSv02,
        feature_level=opensmile.FeatureLevel.LowLevelDescriptors)
    # silme=opensmile.Smile(
       # #feature_set='/mount/arbeitsdaten31/studenten1/team-lab-phonetics/2023/student_directories/lin/sum23lab/lib64/python3.10/site-packages/opensmile/core/config/egemaps/v02_mfcc/eGeMAPSv02.conf',
       # feature_set='/mount/arbeitsdaten31/studenten1/team-lab-phonetics/2023/student_directories/lin/sum23lab/lib/python3.10/site-packages/opensmile/core/config/egemaps/v02_mfcc/eGeMAPSv02.conf',
       # feature_level='lld')
    features_LLDs=silme.process_signal(signal, sampling_rate)
    return  features_LLDs.to_dict('list')

#features= extract_features_opensmile_lld( '/mount/arbeitsdaten/studenten1/team-lab-phonetics/2023/data/ALC/ses3045/5433045016_h_00.wav')
#print(features)

def extract_all_lld(input_dir,out_file):
    features_dict={}
    for actor in os.listdir(os.path.join(input_dir)):
        if actor[:4] == 'ses1' or actor[:4] == 'ses3':
            for wav in os.listdir(os.path.join(input_dir, actor)):
                for i in Alist:
                    if wav[8:] == i + '_h_00.wav' or wav[8:] == str(i) + '_h_01.wav' or wav[8:] == str(i) + '_h_02.wav' or wav[8:]==str(i)+'_h_03.wav':
                        features_dict[wav]={}
                        features_dict[wav]['label']=1 #1:A, 0:NA
                        features_dict[wav]['features']= extract_features_opensmile_lld(os.path.join(input_dir, actor,wav))
                        #print(os.path.join(input_dir, actor, wav))
                        pass
        if actor[:4] == 'ses2' or actor[:4] == 'ses4':
            for wav in os.listdir(os.path.join(input_dir, actor)):
                for i in Alist:
                    if wav[8:] == i + '_h_00.wav' or wav[8:] == str(i) + '_h_01.wav' or wav[8:] == str(i) + '_h_02.wav' or wav[8:]==str(i)+'_h_03.wav':
                        features_dict[wav]={}
                        features_dict[wav]['label']=0 #1:A, 0:NA
                        features_dict[wav]['features']= extract_features_opensmile_lld(os.path.join(input_dir, actor,wav))
                        #print(os.path.join(input_dir, actor,wav))
                        pass
    with open(out_file,'w') as out:
        json.dump(features_dict,out,sort_keys=True, indent=1)

Alist=['01','03','06','07','08','09','11','12','13','15','16','17','19','20','21','23','24','29','30']
NAlist=['01','32','26','23','08','29','31','12','13','15','36','24','19','20','41','59','51','50','60']
extract_all_lld( '/mount/arbeitsdaten/studenten1/team-lab-phonetics/2023/data/ALC', '../ALC_lld_features_full.json')


