import pytest
from unittest.mock import AsyncMock, MagicMock
from ..app.users.models import User
from ..app.users.service import get_users, create_user

@pytest.mark.asyncio
async def test_get_users(mock_db: AsyncMock):
    mock_user_1 = User(id=1, name="John Doe")
    mock_user_2 = User(id=2, name="Jane Smith")


    mock_result = MagicMock()
    mock_result.scalars.return_value.all.return_value = [mock_user_1, mock_user_2]

    mock_db.execute.return_value = mock_result

    users = await get_users(mock_db)

    mock_db.execute.assert_called_once()
    assert users == [mock_user_1, mock_user_2]


@pytest.mark.asyncio
async def test_create_user(mock_db: AsyncMock):
    mock_name = "Alice Cooper"
    
    expected_user = User(name=mock_name)

    await create_user(mock_db, mock_name)

    mock_db.add.assert_called_once()
    args, _ = mock_db.add.call_args
    assert args[0].name == expected_user.name
