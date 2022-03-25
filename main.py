from lab_1a import *
from lab_1b import hashtag
from lab_1c import emotikony

# zad1a
print(delete_numbers('Dzisiaj mamy 4 stopnie na plusie, 1 marca 2022 roku'))


# zad1b
print(delete_html('<div><h2>Header</h2> <p>article<b> strong text</b> <a href="">link</a> </p></div> '))

# zad1c
print(delete_punctuation('''Lorem ipsum dolor sit amet, consectetur; adipiscing elit. Sed eget mattis sem. 
Mauris egestas erat quam, ut faucibus eros congue et. In blandit, mi eu porta; lobortis, 
tortor nisl facilisis leo, at tristique augue risus eu risus. '''))

# zad2
print(hashtag('''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed #texting eget mattis sem. 
Mauris #frasista egestas erat #tweetext quam, ut faucibus eros #frasier congue et. In blandit, mi eu porta
lobortis, tortor nisl facilisis leo, at tristique #frasistas augue risus eu risus.'''))

# zad3
print(emotikony('''To jest tekst :) zawierajacy emotikony :-) :> i smutne też ;< :( :-('''))