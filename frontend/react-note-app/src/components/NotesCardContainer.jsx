import React from 'react'
import NoteCard from './NoteCard'

const NoteCardContainer = ({notes}) => {
  return (
    <div className="container">
    <div className="note-has-grid row">
        <h3> Note Card!  </h3>
        <NoteCard   />
        <NoteCard   />
        <NoteCard   />
        <NoteCard   />
        <NoteCard   />

    </div>
    </div>
  )
}

export default NoteCardContainer