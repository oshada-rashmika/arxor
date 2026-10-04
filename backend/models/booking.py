import enum
import uuid
from datetime import datetime
from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, Numeric
from sqlalchemy.dialects.postgresql import ENUM, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from models.customer_profile import CustomerProfile
    from models.experience import Experience

try:
    from core.database import Base
except ImportError:
    from backend.core.database import Base


class BookingStatus(str, enum.Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"
    COMPLETED = "completed"
    pending = "pending"
    confirmed = "confirmed"
    cancelled = "cancelled"
    completed = "completed"


booking_status_enum = ENUM(
    BookingStatus,
    name="booking_status",
    values_callable=lambda obj: [e.value for e in obj],
    create_type=True,
)


class PaymentStatus(str, enum.Enum):
    UNPAID = "unpaid"
    PENDING = "pending"
    PAID = "paid"
    FAILED = "failed"
    REFUNDED = "refunded"
    unpaid = "unpaid"
    pending = "pending"
    paid = "paid"
    failed = "failed"
    refunded = "refunded"


payment_status_enum = ENUM(
    PaymentStatus,
    name="payment_status",
    values_callable=lambda obj: [e.value for e in obj],
    create_type=True,
)


class Booking(Base):
    __tablename__ = "bookings"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    experience_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("experiences.id"),
        nullable=False,
        index=True,
    )
    customer_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("customer_profiles.user_id"),
        nullable=False,
        index=True,
    )
    status: Mapped[BookingStatus] = mapped_column(
        booking_status_enum,
        default=BookingStatus.PENDING,
        server_default="pending",
        nullable=False,
    )
    slot_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        index=True,
    )
    total_price: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        default=Decimal("0.00"),
        server_default="0",
        nullable=False,
    )
    payment_status: Mapped[PaymentStatus] = mapped_column(
        payment_status_enum,
        default=PaymentStatus.UNPAID,
        server_default="unpaid",
        nullable=False,
    )

    experience: Mapped["Experience"] = relationship(
        "Experience",
        back_populates="bookings",
    )
    customer: Mapped["CustomerProfile"] = relationship(
        "CustomerProfile",
        back_populates="bookings",
    )
