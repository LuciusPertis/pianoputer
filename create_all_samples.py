from scipy.io import wavfile as wf
import numpy as np
import os

'''
files and directory required
-- folders
--- Loud
--- Med
--- Soft

inside these folder should be all C notes of seven octaves in C-Major and
each note should have 2 files, for open and closed pedal sounds

hardcode the selection of files



file will be saved with the filename format as --

"./SAMPLES_ALL/octave_{}/NOTE_O_{}_S_{}_K_{}_P_{}.wav".format(octave_num, octave_num, semitone, key_press, pedal_state)

octave_num in range(1,7+1)
key_press = ('h', 'n', 's') : ('hard', 'natural', 'soft')
pedal_state = ('0', '1') : (open_string, 'restricted_string')

'''

#start by loading all the C notes
class key:
    def __init__(self, filename=None, sndarr=None, octave_num=-1, key_press=-1, pedal_state=-1):
        self.octave_num = octave_num
        self.key_press = key_press
        self.pedal_state = pedal_state

        self.filename = filename
        self.sndarr = sndarr

        
        self.file_exsits = 0

note_names = (  'C{}', 'c{}#', 'D{}', 'd{}#', 'E{}', 'F{}', 'f{}#', 'G{}', 'G{}#',
                'A{}', 'a{}#', 'B{}'  )

master_dir = './Samples_All/'
dirs = ( ('h','Loud'), ('n','Med'), ('s', 'Soft'))
master_save_dir = './MASTER_SAMPLE/'
os.mkdir(master_save_dir)

for d in dirs:
        
    l = os.listdir(master_dir+d[1])

    for file in l:
        print('> > reading file: {}'.format(file))
        
        fps, sndarr = wf.read(master_dir+d[1]+'/'+file)

        key_press = d[0]

        #pedal state
        if '_1' in file:
            pedal_state = 0
        else:
            pedal_state = 1

        #octave
        idx = file.rfind('C')
        octave = int(file[idx+1])

        print('> > read complete : octave={}, pedal_state={}, key_press={}'
              .format(octave, pedal_state, key_press))

        #start pitchshift
        print('> > Starting pitchshit')

        if octave < 2:
            smtones = range(0, 8)
        elif octave < 7:
            smtones = range(-4, 8)
        elif octave == 7:
            smtones = range(-4, 0+1)

        for n in smtones:
            shiftarr = pitchshift2(sndarr, n)

            if n <0:
                octave_num = octave -1
                semitone = 12 + n
            else:
                octave_num = octave
                semitone = n
            
            filename = "NOTECODE_{}_O_{}_S_{}_K_{}_P_{}- note {}.wav".format(
                                    (octave_num-1)*12 + semitone
                                    , octave_num
                                    , semitone
                                    , key_press
                                    , pedal_state
                                    , note_names[semitone].format(octave_num)
                                    )

            wf.write(master_save_dir+filename, fps, shiftarr)

            print('> > > written : {}'.format(filename))

            
        
        


