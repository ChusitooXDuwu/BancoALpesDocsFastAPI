import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [documentos, setDocumentos] = useState([]);
  const [tipo, setTipo] = useState('');
  const [estado, setEstado] = useState('');
  const [archivo, setArchivo] = useState('');
  const [clienteId, setClienteId] = useState(1);

  // Cargar documentos al montar el componente
  useEffect(() => {
    axios.get('http://127.0.0.1:8000/documentos/')
      .then(response => {
        setDocumentos(response.data);
      })
      .catch(error => {
        console.error("Error al obtener los documentos!", error);
      });
  }, []);

  // Manejar envío del formulario
  const handleSubmit = (event) => {
    event.preventDefault();
    axios.post('http://127.0.0.1:8000/documentos/', {
      cliente_id: clienteId,
      tipo: tipo,
      estado: estado,
      archivo: archivo,
    })
    .then(response => {
      setDocumentos([...documentos, response.data]);
      setTipo('');
      setEstado('');
      setArchivo('');
    })
    .catch(error => {
      console.error("Error al crear el documento!", error);
    });
  };

  return (
    <div className="App">
      <h1>Documentos</h1>
      <ul>
        {documentos.map(doc => (
          <li key={doc.id}>{doc.tipo} - {doc.estado} - {doc.archivo}</li>
        ))}
      </ul>
      <form onSubmit={handleSubmit}>
        <label>
          Tipo:
          <input type="text" value={tipo} onChange={e => setTipo(e.target.value)} />
        </label>
        <label>
          Estado:
          <input type="text" value={estado} onChange={e => setEstado(e.target.value)} />
        </label>
        <label>
          Archivo:
          <input type="text" value={archivo} onChange={e => setArchivo(e.target.value)} />
        </label>
        <button type="submit">Crear Documento</button>
      </form>
    </div>
  );
}

export default App;
