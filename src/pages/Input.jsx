import React, { useState } from 'react'

import { useNavigate } from 'react-router-dom'

const Input = () => {

  const navigate = useNavigate();

  let fileName = "default.jpg"
  let filePath = "./static/images/"
  const [selectedFile, setSelectedFile] = useState(null);
  const [displayImage, setDisplayImage] = useState("./static/images/default.jpg")

  const fileChangeHandler = (e) => {
    setSelectedFile(e.target.files[0]);
    console.log(e.target.files[0]);
    console.log(e.target.files[0].lastModified);
  }

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append(
      "file",
      selectedFile,
      selectedFile.name
    );

    try {
      const endpoint = "http://localhost:8000/uploadImage/";
      const response = await fetch(endpoint, {
        // mode: 'no-cors',// change here
        method: "POST",
        body: formData
      });

      if (response.ok) {
        console.log("File uploaded successfully ! :) ");
        console.log(response);

        const data = await response.json();
        fileName = data.fileName;

        console.log("File name : ", fileName);
        setDisplayImage(filePath + fileName);
        console.log(displayImage);

      } else {
        console.log(response);
        console.log("Failed to upload the file :( ");
      }
    }
    catch (error) {
      console.log(error);
    }
    console.log(selectedFile.name);


    // trying to add navigate function on clicking the upload button

    navigate('/sidebar')
  }


  return (
    <div id='input'>
      <h1>Input section!</h1>

      <div className="form-control w-full max-w-xs">
        <form action="">
        
          <label className="label">
            <span className="label-text">Pick a file</span>
            <span className="label-text-alt">Alt label</span>
          </label>
          <input onChange={fileChangeHandler} type="file" name="image" accept=".jpeg, .jpg, .png" className="file-input file-input-bordered w-full max-w-xs" />
          <label className="label">
            <span className="label-text-alt">Alt label</span>
            <span className="label-text-alt">(.jpg, .jpeg, .png)</span>
          </label>
          <button onClick={handleSubmit} className="btn btn-outline">Upload</button>
        </form>
      </div>
      {selectedFile && <h3>{selectedFile.name}</h3>}

      <h3>{displayImage}</h3>
    </div>
  )
}

export default Input
