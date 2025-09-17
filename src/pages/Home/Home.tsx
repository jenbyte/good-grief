import React from 'react'
import Card from '../../components/Card/Card'
import Offers from '../Offers/Offers'

type HomeProps = {
}

const Home: React.FC<HomeProps> = ({}) => {
  return (
    <div className=''>
        <div>
            <div className=''></div>
            <h1>Hi, how are you feeling today?</h1>

            <div>
                <Card />
            </div>
      
      </div>

      <div>
        <h2 
            className="cursor-pointer hover:underline"
            role="link"
            tabIndex={0}
            // onClick={go}
            // onKeyDown={(e) => e.key === "Enter" && go()
        >
            Offers
        </h2>
        <div>
            <Card />
        </div>
      </div>
    </div>
  )
}

export default Home
