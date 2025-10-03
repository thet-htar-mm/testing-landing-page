import pytest
from unittest.mock import AsyncMock, MagicMock
# from ..app.users.models import User
from ..app.users.service import get_users, create_user

# @pytest.mark.asyncio
# async def test_get_users(mock_db: AsyncMock):
#     mock_user_1 = User(id=1, name="John Doe")
#     mock_user_2 = User(id=2, name="Jane Smith")


#     mock_result = MagicMock()
#     mock_result.scalars.return_value.all.return_value = [mock_user_1, mock_user_2]

#     mock_db.execute.return_value = mock_result

#     users = await get_users(mock_db)

#     mock_db.execute.assert_called_once()
#     assert users == [mock_user_1, mock_user_2]


# @pytest.mark.asyncio
# async def test_create_user(mock_db: AsyncMock):
#     mock_name = "Alice Cooper"
    
#     expected_user = User(name=mock_name)

#     await create_user(mock_db, mock_name)

#     mock_db.add.assert_called_once()
#     args, _ = mock_db.add.call_args
#     assert args[0].name == expected_user.name

import pytest
from unittest.mock import AsyncMock, MagicMock
from ..app.users.service import get_users, create_user

@pytest.mark.asyncio
async def test_get_users_raw_sql(mock_db: AsyncMock):
    # Mock rows returned by raw SQL
    mock_row_1 = (1, "John Doe") 
    mock_row_2 = (2, "Jane Smith")

    # Mock result of db.execute()
    mock_result = MagicMock()
    mock_result.fetchall.return_value = [mock_row_1, mock_row_2]

    mock_db.execute.return_value = mock_result

    users = await get_users(mock_db)

    mock_db.execute.assert_called_once()
    assert users == [mock_row_1, mock_row_2]


@pytest.mark.asyncio
async def test_create_user_raw_sql(mock_db: AsyncMock):
    mock_name = "Alice Cooper"

    mock_inserted_row = (1, mock_name)
    mock_result = MagicMock()
    mock_result.fetchone.return_value = mock_inserted_row
    mock_db.execute.return_value = mock_result
    mock_db.commit = AsyncMock()

    inserted_user = await create_user(mock_db, mock_name)

    assert mock_db.execute.call_count == 1
    args, kwargs = mock_db.execute.call_args
    assert "INSERT INTO users" in args[0].text
    assert args[1]["name"] == mock_name

    mock_db.commit.assert_awaited_once()
    assert inserted_user == mock_inserted_row
