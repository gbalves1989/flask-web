from werkzeug.datastructures import FileStorage
from dotenv import load_dotenv
from web import app
import uuid
import os


load_dotenv()


def storage_file(file: FileStorage) -> str:
    root, ext = file.filename.split('.')
    filename: str = str(uuid.uuid4())

    file.save(
        os.path.join(
            app.root_path,
            'static',
            os.environ.get('UPLOAD_FOLDER'),
            f"{filename}.{ext}"
        )
    )

    return f"{filename}.{ext}"


def storage_delete_file(filename: str) -> None:
    os.remove(
        os.path.join(
            app.root_path,
            'static',
            os.environ.get('UPLOAD_FOLDER'),
            filename
        )
    )
