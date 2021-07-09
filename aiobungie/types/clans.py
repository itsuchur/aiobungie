'''
MIT License

Copyright (c) 2020 - Present nxtlo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
from typing import TypedDict, Dict, Any, List, Union
from ..utils import Image
from .user import UserCard
from datetime import datetime

class ClanOwner(UserCard, total=False):
	joinDate: datetime
	groupId: int
	destinyUserInfo: Dict[str, Any] # TODO: Make this Dict[str, ClanOwnerResponse]

class PartitialClan(TypedDict):
	groupId: int
	memberCount: int
	name: str
	about: str
	motto: str
	tags: List[str]
	description: str
	isPublic: bool
	bannerPath: Image
	avatarPath: Image
	creationDate: datetime

class ClanResponse(PartitialClan):
	detail: Dict[str, PartitialClan]
	founder: ClanOwner
	ErrorCode: int

class Clan(ClanResponse, total=False):
	Response: Dict[str, ClanResponse]