import React from "react";

import aboutT  from "../../src/aboutText.json";
import test2  from "../../src/assets/pageText/test.json";



function multiLanguage(isSWE, test) {
    if(isSWE){
        return test.map((test) =>(
            <div className='border m-2'>
                <h3>{test.swe}</h3>
            </div>
        ))
    }
    return test.map((test) =>(
        <div className='border m-2'>
            <h3>{test.eng}</h3>
        </div>
    ))
}

export default multiLanguage

{/*
function multiLanguage() {
    var temp = ""
    fetch(`${aboutT}.json`)
        .then(response => response.json())
        .then(data => {temp = new data.swe})


    return temp;
}

export default multiLanguage

{/*
    if(isSWE){
        var temp2 = "aboutT.swe";
        {aboutT.map(({swe}) => (

            <div>
                <h3 >{swe}</h3>
            </div>))}
        return temp
    }
    */}



