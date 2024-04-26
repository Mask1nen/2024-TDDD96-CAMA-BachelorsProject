
import {useState} from "react";

function multiLanguage(isSWE, test) {
    //const [isSWE2, setIsSWE2] = useState(false);

    if(isSWE){
        return test.map((test) =>(
            <h3>{test.swe}</h3>
        ))
    }
    return test.map((test) =>(
        <h3>{test.eng}</h3>
    ))    
}


export default multiLanguage