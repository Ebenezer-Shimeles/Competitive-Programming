function sortSentence(s: string): string {
    const shuffledSentences = s.split(' ');
    const unShuffledSentencesArray= (new Array(shuffledSentences.length));
    
    for(const shuffledWord of shuffledSentences){
        const num = Number(shuffledWord[shuffledWord.length- 1]);
        console.log({num})
        
        unShuffledSentencesArray[num - 1] = shuffledWord.substring(0, shuffledWord.length-1)
    }
    let str = ""
    for(const word of unShuffledSentencesArray) str += word + " "
    return str.substring(0, str.length-1);
};