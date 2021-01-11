from fastapi import HTTPException, status

DataSetKeyValueError = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Value not found in dataset",
)
