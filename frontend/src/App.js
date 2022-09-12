import React from 'react'
import './App.css'
import { useState } from 'react'
function App() {
  const [photo, setPhoto] = useState('')
  const [viewFile, setViewFile] = useState('')

  const handleChange = (e) => {
    e.preventDefault();
    if (e.target.files[0]) {
        if (e.target.files[0].type.match(/image-*/)) {
            setPhoto(e.target.files[0]);
            setViewFile(URL.createObjectURL(e.target.files[0]))
        }
        else {
            alert('Not an image file')
        }
    }
}
  return (
    <div className='app'>
      <div className="app_header">
        <h1>Grayscale Colorizer</h1>
        <hr />
      </div>
      <div className="app_remaining">
        <div className="app_remaining_left">
        {photo===''?<input type="file" accept="image/*" id="image" alt="Grayscale photo" onChange={handleChange} required></input>: <img src={viewFile} style={{ height: '100%', width: '100%' }} alt="Uploaded" />
}
        </div>
        <div className='app_button'>
          Convert
        </div>
        <div className="app_remaining_right">
          <h4>Converted RGB image</h4>
        </div>
      </div>
    </div>
  )
}

export default App