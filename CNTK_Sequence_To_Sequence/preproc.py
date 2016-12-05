"""
Preprocess Corpus
"""
#%%
LINE_DICT = {}
LINE_FILE = "cornell movie-dialogs corpus\\movie_lines.txt"
with open(LINE_FILE) as line_file:
    for line in line_file:
        (lineId, charId, movId, charName, rawLine) = line.split(sep=" +++$+++ ")
        LINE_DICT[str(lineId)] = rawLine.strip()
print(LINE_DICT)

#%%
DISCOURSE_NUMBER = 0
CONV_FILE = "cornell movie-dialogs corpus\\movie_conversations.txt"
with open(CONV_FILE) as conv_file:
    for line in conv_file:
        diag_list = line.split(sep=" +++$+++ ")[-1].strip()
        diag_list = diag_list.replace("[", "").replace("]", "")
        diag_list = diag_list.replace("'", "").replace(" ", "")
        for diag in diag_list.split(sep=","):
            print("d" + str(DISCOURSE_NUMBER) + ":" + LINE_DICT[diag])
        DISCOURSE_NUMBER = DISCOURSE_NUMBER + 1
