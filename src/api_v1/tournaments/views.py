import asyncio
import uuid

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse

from sqlalchemy.ext.asyncio import AsyncSession

from src.models import db_helper

from src.api_v1.tournaments.service_tournament.Tour_Buffer import TOURNAMENT_BUFFER
from .schemas import CreateTournament
from .crud import get_tournaments_members
from .service_tournament.Tour_Manager import Tournament


router = APIRouter(
    tags=["Tournaments"]
)


@router.post(
    path="/create_tournament"
)
async def create_tournament(
        members_list: list[uuid.UUID],
        tables_list: list[int],
        session: AsyncSession = Depends(db_helper.get_scoped_session_dependency),
):
    members = await get_tournaments_members(
        members_list=members_list,
        session=session
    )

    tournament = Tournament(
        members=members,
        tournament_type="standard",
        tables=tables_list,
        session=session
    )
    print(id(TOURNAMENT_BUFFER))
    TOURNAMENT_BUFFER[tournament.tour_id] = tournament
    print("Tournament created: users:", TOURNAMENT_BUFFER.get(tournament.tour_id).members)
    print(TOURNAMENT_BUFFER)
    print(id(TOURNAMENT_BUFFER))
    return tournament.tour_id


@router.post(
    path="/start/"
)
async def start_tournament(
        tournament_id: uuid.UUID
):
    response = JSONResponse(content={'message': 'tournament_starting...'}, status_code=200)

    current_tournament = TOURNAMENT_BUFFER.get(tournament_id)
    asyncio.create_task(current_tournament.start_tournament())

    return response


@router.post(
    path="/complete_game"
)
async def complete_game(
        table_number: int,
        tournament_id: uuid.UUID
):
    current_tournament = TOURNAMENT_BUFFER.get(tournament_id)
    current_tournament.engine.table_operator.remove_game_from_table(table_number=table_number)