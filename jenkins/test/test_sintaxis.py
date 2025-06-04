import py_compile
import os

def test_syntax_etl_script():
    """
    Verifica que el script principal no tenga errores de sintaxis.
    """
    script_path = os.path.join("src", "etl_proveedores.py")
    try:
        py_compile.compile(script_path, doraise=True)
    except py_compile.PyCompileError as e:
        pytest.fail(f"Error de sintaxis en {script_path}: {e}")
