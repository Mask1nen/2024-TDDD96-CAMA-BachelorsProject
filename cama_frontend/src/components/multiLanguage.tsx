{/*This file conatins the code responible for controlling the multi language function

    multiLanguage(isSWE, test) takes in two parameters:
    isSWE; that is a boolian if the target language is swedich or not (then eng)
    text; that will be displayed. This text is in a json file.

*/}


function multiLanguage(isSWE, text) {

    if(isSWE){
        return text.map((text) =>(
            <div>{text.swe}</div>
        ))
    }
    return text.map((text) =>(
        <div>{text.eng}</div>
    ))    
}


export default multiLanguage