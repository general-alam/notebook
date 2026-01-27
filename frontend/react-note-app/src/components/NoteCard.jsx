import React from 'react'
import { MdMarkunread } from "react-icons/md";
import { FaNoteSticky } from "react-icons/fa6";

const NoteCard = () => {

  return (
    <div className="col-md-4 single-note-item all-category">
      <div className="card card-body">
        <span className="side-stick" style={{ backgroundColor: "blue" }}></span>
        <FaNoteSticky style={{ marginLeft: "auto", color: "blue" }} />
        <a href={'/notes-detail'} style={{textDecoration: "none", color: "black"}}>
        <h5
          className="note-title text-truncate w-75 mb-0"
          data-noteheading="Wow! This is a note title!"
        >
          Wow! This is a note title! {" "}
        </h5>
        </a>
        
        <p className="note-date font-12 text-muted">27th January 2026</p>
        <div className="note-content">
          <p
            className="note-inner-content text-muted"
            data-notecontent="This is the body of the text, actually, it can be anything you want.."
          >
           This is the body of the text, actually, it can be anything you want.
          </p>
        </div>
        <div className="d-flex align-items-center">
       

          <span className="d-flex justify-contents-around">
            <a href="/notes-detail">
              <MdMarkunread
                style={{ fontSize: "25px", cursor: "pointer", color: "blue" }}
              />
            </a>

            <small className="text-muted">WORK</small>
          </span>
        </div>
      </div>
    </div>
  )
}

export default NoteCard