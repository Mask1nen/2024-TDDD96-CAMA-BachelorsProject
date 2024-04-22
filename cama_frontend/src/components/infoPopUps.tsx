import './infoPopUps.css'

function infoPopUps(props){
    return(props.trigger) ? (
        <div className='infoPopUp'>
            <div className='infoPopUp-inner'>
                <button className='close-botton' onClick={() => props.setTrigger(false)} style={{ color: 'white' }}>close</button>
                { props.children }
            </div>
        </div>
    ): "";
}

export default infoPopUps