import React from 'react'
import styles from './Card.module.css'

type CardProps = {

}

const Card: React.FC<CardProps> = ({}) => {
  return (
    <div className={`${styles.card} rounded-xl mt-4 mb-8 p-5`}>
      <h3>Featured Meditaiton</h3>
    </div>
  )
}

export default Card
