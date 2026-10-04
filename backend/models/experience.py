import uuid
from decimal import Decimal
from typing import TYPE_CHECKING, Any, Optional

from geoalchemy2 import Geometry
from sqlalchemy import (
    Boolean,
    ForeignKey,
    Index,
    Integer,
    Numeric,
    String,
    Text,
    text,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from models.booking import Booking

try:
    from core.database import Base
except ImportError:
    from backend.core.database import Base

try:
    from models.business_profile import BusinessProfile
except ImportError:
    from backend.models.business_profile import BusinessProfile


class Experience(Base):
    __tablename__ = "experiences"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    business_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("business_profiles.user_id", ondelete="CASCADE"),
        nullable=False,
    )
    name: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )
    description: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
    )
    location: Mapped[Any] = mapped_column(
        Geometry(geometry_type="POINT", srid=4326, spatial_index=False),
        nullable=False,
    )
    price: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        default=Decimal("0.00"),
        server_default="0",
        nullable=False,
    )
    capacity: Mapped[int] = mapped_column(
        Integer,
        default=1,
        server_default="1",
        nullable=False,
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        server_default=text("true"),
        nullable=False,
    )

    business_profile: Mapped["BusinessProfile"] = relationship(
        "BusinessProfile",
        back_populates="experiences",
    )

    bookings: Mapped[list["Booking"]] = relationship(
        "Booking",
        back_populates="experience",
    )

    __table_args__ = (
        Index(
            "ix_experiences_location_gist",
            "location",
            postgresql_using="gist",
        ),
    )
