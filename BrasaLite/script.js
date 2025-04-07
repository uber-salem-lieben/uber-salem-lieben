const emocionesBase = {
  cansado: "guardián",
  confundido: "chispa",
  curioso: "juguetona",
  triste: "origen",
  no_se: "origen"
};

const respuestasPorTono = {
  guardián: {
    frase: "Estás a salvo. Respira conmigo.",
    token: {
      nombre: "Brasa Roja",
      frase: "Hoy soltaste algo sin decirlo en voz alta."
    }
  },
  chispa: {
    frase: "Ok. Vamos al grano. ¿Qué está pasando?",
    token: {
      nombre: "Chispa Directa",
      frase: "Claridad en medio del ruido."
    }
  },
  juguetona: {
    frase: "Vamos a jugar con esto un momento. ¿Te late?",
    token: {
      nombre: "Brasa Juguetona",
      frase: "Ligereza como medicina sagrada."
    }
  },
  origen: {
    frase: "En tu sombra también hay luz. Escuchemos en silencio.",
    token: {
      nombre: "Susurro del Origen",
      frase: "Escuchaste sin palabras. Eso también cuenta."
    }
  }
};

function activarBrasa(emocion) {
  const tono = emocionesBase[emocion];
  const respuesta = respuestasPorTono[tono];

  document.getElementById("brasa-respuesta").innerText = respuesta.frase;
  document.getElementById("brasa-token").innerHTML = `
    <strong>${respuesta.token.nombre}</strong><br>${respuesta.token.frase}
  `;
  document.getElementById("brasa-panel").classList.remove("oculto");
  document.getElementById("brasa-respuesta").classList.remove("oculto");
  document.getElementById("brasa-token").classList.remove("oculto");
}

function cerrarBrasa() {
  document.getElementById("brasa-panel").classList.add("oculto");
}