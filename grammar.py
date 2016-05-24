from nltk import *

def main():
  
  ugrammar = grammar.FeatureGrammar.fromstring("""
  S -> NP[AGR=?a] VP[SUBCAT=nil, AGR=?a, FORM=vbz]  
  S -> NP[AGR=?a] VP[SUBCAT=nil, AGR=?a, FORM=pret]
  S -> S Conj S | Int Q | Q | AP S
  
  Q -> Verb[SUBCAT=?a, AGR=?a] NP[AGR=?a] VP[SUBCAT=[HEAD=?arg, TAIL=?rest], FORM=vbz]
  
  VP[SUBCAT=?rest, AGR=?a, FORM=vbz] -> Verb[SUBCAT=[HEAD=?arg, TAIL=?rest], AGR=?a, FORM=vbz] ARG[CAT=?arg]
  VP[SUBCAT=?rest, AGR=?a, FORM=vbz] -> Verb[SUBCAT=nil, AGR=?a, FORM=vbz]    
  VP[AGR=?a, FORM=vbz] -> Verb[AGR=?a, FORM=vbz] S 
  VP[AGR=?a, FORM=vbz] -> Adv VP[AGR=?a, FORM=vbz]
  
  VP[SUBCAT=?rest, AGR=?a, FORM=pret] -> Verb[SUBCAT=[HEAD=?arg, TAIL=?rest], AGR=?a, FORM=pret] ARG[CAT=?arg]
  VP[AGR=?a, FORM=pret] -> Verb[AGR=?a, FORM=pret] Conj VP[AGR=?a, FORM=pret]
  VP[AGR=?a, FORM=pret] -> VP[AGR=?a, FORM=pret] Conj VP[AGR=?a, FORM=pret]
  
  VP[SUBCAT=?rest, FORM=base] -> Verb[SUBCAT=?a, FORM=base] NP
  
  ARG[CAT=NP] -> NP
  ARG[CAT=PP] -> PP

  NP[AGR=?a] -> Noun[AGR=?a] | ProperNoun[AGR=?a] |  Adj ProperNoun[AGR=?a]
  NP[AGR=?a] -> Det[AGR=?a] Noun[AGR=?a] | Det[AGR=?a] SingNoun[AGR=?a] 
  NP[AGR=?a] -> Det[AGR=?a] Adj Noun[AGR=?a] | Det[AGR=?a] Adj SingNoun[AGR=?a]
  NP[AGR=?a] -> NP[AGR=?a] PP
  NP[AGR=?a] -> NP[AGR=?a] Verb[SUBCAT=?a, FORM=pres] NP[AGR=?a]  
  
  NP[AGR=[NUM=plur]] -> NP Conj NP
  
  ProperNoun[AGR=[NUM=sing, PER=3]] -> "Guinevere" | "Arthur"
  ProperNoun[AGR=[NUM=plur, PER=3]] -> "Mondays"
  Noun[AGR=[NUM=plur]] -> "horses"
  Noun[AGR=[NUM=sing]] -> "water" |"milk" | "spots" 
  SingNoun[AGR=[NUM=sing]] -> "horse" | "castle" | "chalice"
  
  Verb[SUBCAT=[HEAD=NP, TAIL=nil], AGR=[NUM=sing, PER=3], FORM=vbz] -> "drinks" | "does" | "thinks" | "rides" | "sees" 
  Verb[SUBCAT=[HEAD=PP, TAIL=nil], AGR=[NUM=sing, PER=3], FORM=vbz] ->  "smiles" | "drinks" | "rides" | "thinks" 
  Verb[SUBCAT=nil, AGR=[NUM=sing, PER=3], FORM=vbz] -> "smiles" | "rides" | "drinks" | "thinks"
  
  Verb[AGR=[NUM=sing, PER=1], FORM=vbz] -> "smile" | "ride" | "drink"| "think"
  Verb[AGR=[NUM=plur], FORM=vbz] -> "smile" | "ride" | "drink" | "think" 
  
  Verb[SUBCAT=[HEAD=NP, TAIL=[HEAD=VP, TAIL=nil]], AGR=[NUM=plur], FORM=base] -> "do"
  
  Verb[AGR=[NUM=sing], FORM=pret] -> "rode" | "drank" 
  Verb[AGR=[NUM=plur], FORM=pret] -> "rode" | "drank"
  
  Verb[SUBCAT=[HEAD=NP, TAIL=nil], FORM=pres] -> "riding"
  Verb[SUBCAT=[HEAD=PP, TAIL=nil], FORM=pres] -> "riding"
  Verb[SUBCAT=nil, FORM=pres] -> "riding"
    
  PP -> Prep NP
  AP -> Aux S
  
  Det -> "the" |  "his"
  Conj -> "and"
  Int -> "when" | "where" | "what"
  Adj -> "old" | "white"
  Adv -> "often" | "seldom"
  Prep -> "on" | "near" | "to" | "from" | "with"
  Aux -> "when" 
  """)
  
  uparser = FeatureChartParser(ugrammar)
  
  text = """\
  Guinevere smiles
  Guinevere and Arthur smile
  horses drink water
  Arthur rides the horse
  Guinevere rides on Mondays
  Arthur often rides
  Guinevere rides the old horse near the castle 
  Guinevere seldom drinks milk
  when Arthur drinks milk Guinevere smiles
  Guinevere thinks Arthur often rides the horse
  Arthur rode to the castle and drank from his chalice
  Arthur rode and drank water and milk
  where do Arthur and Guinevere ride on Mondays
  when does Guinevere ride
  Arthur ride
  Arthur smiles Guinevere
  when do Guinevere smiles
  """
  
  #Extension sentences
  #Arthur rides the horse with the white spots near the castle
  #Arthur sees Guinevere riding the horse
  #what does Guinevere think Arthur drinks
  #does Guinevere think Arthur seldom drinks water
  
  sents = text.splitlines()
  
  for sent in sents:
    print "Sentence: " + sent
    parses = uparser.parse(sent.split())
    count_sents = 0
    for tree in parses:
        print tree, "\n"
        count_sents += 1
    print "Number of trees: ", count_sents

if __name__ == '__main__':
  main()
