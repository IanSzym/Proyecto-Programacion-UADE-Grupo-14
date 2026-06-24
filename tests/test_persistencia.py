import json

import persistencia


def test_guardar_y_cargar_datos(tmp_path, monkeypatch):
    archivo_falso = tmp_path / "persistencia.py"
    archivo_falso.write_text("")
    monkeypatch.setattr(persistencia, "__file__", str(archivo_falso))

    datos = [{"id": 1, "nombre": "Ana"}]

    persistencia.guardar_datos("prueba.json", datos)
    datos_cargados = persistencia.cargar_datos("prueba.json", [])

    assert datos_cargados == datos


def test_cargar_datos_crea_archivo_si_no_existe(tmp_path, monkeypatch):
    archivo_falso = tmp_path / "persistencia.py"
    archivo_falso.write_text("")
    monkeypatch.setattr(persistencia, "__file__", str(archivo_falso))

    datos_iniciales = []
    resultado = persistencia.cargar_datos("nuevo.json", datos_iniciales)

    ruta = tmp_path / "data" / "nuevo.json"

    assert resultado == []
    assert ruta.exists()
    assert json.loads(ruta.read_text(encoding="utf-8")) == []


def test_cargar_datos_reinicia_json_con_error(tmp_path, monkeypatch):
    archivo_falso = tmp_path / "persistencia.py"
    archivo_falso.write_text("")
    monkeypatch.setattr(persistencia, "__file__", str(archivo_falso))

    carpeta_datos = tmp_path / "data"
    carpeta_datos.mkdir()
    ruta = carpeta_datos / "roto.json"
    ruta.write_text("{texto roto", encoding="utf-8")

    datos_iniciales = [{"id": 1}]
    resultado = persistencia.cargar_datos("roto.json", datos_iniciales)

    assert resultado == datos_iniciales
    assert json.loads(ruta.read_text(encoding="utf-8")) == datos_iniciales
