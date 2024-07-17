# async def current_user(
#     session: AsyncSession = Depends(get_session),
#     token: str = Depends(OAUTH2),
# ) -> User:
#     try:
#         payload = decode(token, TOKEN_SECRET, algorithms=[TOKEN_ALGORITHM])
#         username: str = payload["sub"]

#         if not username:
#             Credentials.raise_exception()

#         token_data = TokenData(username=username)

#     except (DecodeError, KeyError):
#         Credentials.raise_exception()

#     statement = select(User).where(User.email == token_data.username)
#     result = await session.exec(statement)
#     user = result.one_or_none()

#     if not user:
#         Credentials.raise_exception()

#     return user
