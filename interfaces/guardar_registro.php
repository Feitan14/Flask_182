<?php
$servername = "admin.html";
$username = "nombre";
$password = "contraseña";
$dbname = "nombre_de_la_base_de_datos";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Error de conexión: " . $conn->connect_error);
}

$rfc = $_POST['rfc'];
$nombre = $_POST['nombre'];
$apellido_paterno = $_POST['apellido_paterno'];
$apellido_materno = $_POST['apellido_materno'];
$cedula = $_POST['cedula'];
$correo = $_POST['correo'];
$contrasena = $_POST['contrasena'];
$opcion = $_POST['opcion'];

$sql = "INSERT INTO registros (rfc, nombre, apellido_paterno, apellido_materno, cedula, correo, contrasena, opcion) VALUES ('$rfc', '$nombre', '$apellido_paterno', '$apellido_materno', '$cedula', '$correo', '$contrasena', '$opcion')";

if ($conn->query($sql) === TRUE) {
    echo "Registro guardado correctamente";
} else {
    echo "Error al guardar el registro: " . $conn->error;
}

$conn->close();
?>
