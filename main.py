
from datetime import date, timedelta

from app.model.member import Member
from app.model.trainer import Trainer
from app.model.exercise import Exercise
from app.model.workout import Workout
from app.model.membership import Membership
from app.model.payment import CashPayment, CardPayment

from app.repositories.member_repository import MemberRepository
from app.repositories.trainer_repository import TrainerRepository
from app.repositories.exercise_repository import ExerciseRepository
from app.repositories.workout_repository import WorkoutRepository
from app.repositories.membership_repository import MembershipRepository
from app.repositories.payment_repository import PaymentRepository

from app.services.member_service import MemberService
from app.services.trainer_service import TrainerService
from app.services.exercise_service import ExerciseService
from app.services.workout_service import WorkoutService
from app.services.membership_service import MembershipService
from app.services.payment_service import PaymentService
from app.services.progress_service import ProgressService

from app.utils.exceptions import FitTrackError


# =========================
# REPOSITORY + SERVICE
# =========================

member_repository = MemberRepository()
member_service = MemberService(member_repository)

trainer_repository = TrainerRepository()
trainer_service = TrainerService(trainer_repository)

exercise_repository = ExerciseRepository()
exercise_service = ExerciseService(exercise_repository)

workout_repository = WorkoutRepository()
workout_service = WorkoutService(workout_repository)

membership_repository = MembershipRepository()
membership_service = MembershipService(membership_repository)

payment_repository = PaymentRepository()
payment_service = PaymentService(payment_repository)


# =========================
# MEMBER
# =========================

def register_member():
    print("\n===== ĐĂNG KÝ MEMBER =====")

    name = input("Tên: ")
    email = input("Email: ")
    phone = input("Số điện thoại: ")
    birth = input("Ngày sinh: ")

    try:
        members = member_repository.get_all()

        if members:
            last_id = max(
                int(member.member_id[1:])
                for member in members
                if member.member_id.startswith("M")
            )
        else:
            last_id = 0

        member_id = f"M{last_id + 1:03d}"

        member = Member(
            name,
            email,
            phone,
            birth,
            member_id,
            True
        )

        member_service.register_member(member)

        print(f"Đăng ký thành công! ID: {member.member_id}")

    except FitTrackError as e:
        print(f"Lỗi: {e}")

    except ValueError as e:
        print(f"Lỗi dữ liệu: {e}")


def list_members():
    print("\n===== DANH SÁCH MEMBER =====")

    members = member_repository.get_all()

    if not members:
        print("Chưa có member.")
        return

    for member in members:
        status = "Đang hoạt động" if member.is_activate else "Đã vô hiệu hóa"

        print(
            f"ID: {member.member_id} | "
            f"Tên: {member.name} | "
            f"Email: {member.email} | "
            f"Trạng thái: {status}"
        )


def deactivate_member():
    print("\n===== VÔ HIỆU HÓA MEMBER =====")

    member_id = input("Nhập Member ID: ")

    if member_service.deactivate_member(member_id):
        print("Đã vô hiệu hóa member.")
    else:
        print("Không tìm thấy member.")


def member_menu():
    while True:
        print("\n========== MEMBER ==========")
        print("1. Đăng ký Member")
        print("2. Danh sách Member")
        print("3. Vô hiệu hóa Member")
        print("0. Quay lại")

        choice = input("Nhập lựa chọn: ")

        if choice == "1":
            register_member()

        elif choice == "2":
            list_members()

        elif choice == "3":
            deactivate_member()

        elif choice == "0":
            break

        else:
            print("Lựa chọn không hợp lệ!")


# =========================
# TRAINER
# =========================

def add_trainer():
    print("\n===== THÊM TRAINER =====")

    name = input("Tên: ")
    email = input("Email: ")
    phone = input("Số điện thoại: ")
    birth = input("Ngày sinh: ")
    specialty = input("Chuyên môn: ")
    experience = int(input("Số năm kinh nghiệm: "))

    trainers = trainer_repository.get_all()

    if trainers:
        last_id = max(
            int(trainer.trainer_id[1:])
            for trainer in trainers
            if trainer.trainer_id.startswith("T")
        )
    else:
        last_id = 0

    trainer_id = f"T{last_id + 1:03d}"

    trainer = Trainer(
        name,
        email,
        phone,
        birth,
        trainer_id,
        specialty,
        experience
    )

    try:
        trainer_service.add_trainer(trainer)
        print(f"Thêm Trainer thành công! ID: {trainer_id}")

    except FitTrackError as e:
        print(f"Lỗi: {e}")


def list_trainers():
    print("\n===== DANH SÁCH TRAINER =====")

    trainers = trainer_service.list_trainers()

    if not trainers:
        print("Chưa có trainer.")
        return

    for trainer in trainers:
        print(
            f"ID: {trainer.trainer_id} | "
            f"Tên: {trainer.name} | "
            f"Chuyên môn: {trainer.specialty} | "
            f"Kinh nghiệm: {trainer.experience__year} năm"
        )


def trainer_menu():
    while True:
        print("\n========== TRAINER ==========")
        print("1. Thêm Trainer")
        print("2. Danh sách Trainer")
        print("0. Quay lại")

        choice = input("Nhập lựa chọn: ")

        if choice == "1":
            try:
                add_trainer()
            except ValueError:
                print("Số năm kinh nghiệm phải là số.")

        elif choice == "2":
            list_trainers()

        elif choice == "0":
            break

        else:
            print("Lựa chọn không hợp lệ!")


# =========================
# EXERCISE
# =========================

def add_exercise():
    print("\n===== THÊM EXERCISE =====")

    name = input("Tên bài tập: ")
    category = input("Nhóm cơ: ")
    description = input("Mô tả: ")

    exercise = Exercise(
        name,
        category,
        description
    )

    exercise_service.add_exercise(exercise)

    print("Thêm bài tập thành công!")


def list_exercises():
    print("\n===== DANH SÁCH EXERCISE =====")

    exercises = exercise_service.list_exercises()

    if not exercises:
        print("Chưa có bài tập.")
        return

    for i, exercise in enumerate(exercises, start=1):
        print(
            f"{i}. {exercise.name} | "
            f"{exercise.category} | "
            f"{exercise.description}"
        )


def exercise_menu():
    while True:
        print("\n========== EXERCISE ==========")
        print("1. Thêm Exercise")
        print("2. Danh sách Exercise")
        print("0. Quay lại")

        choice = input("Nhập lựa chọn: ")

        if choice == "1":
            add_exercise()

        elif choice == "2":
            list_exercises()

        elif choice == "0":
            break

        else:
            print("Lựa chọn không hợp lệ!")


# =========================
# WORKOUT
# =========================

def add_workout():
    print("\n===== THÊM WORKOUT =====")

    member_id = input("Member ID: ")
    date_text = input("Ngày tập (YYYY-MM-DD): ")

    try:
        workout_date = date.fromisoformat(date_text)
    except ValueError:
        print("Ngày không đúng định dạng.")
        return

    workouts = workout_repository.get_all()

    workout_id = f"W{len(workouts) + 1:03d}"

    workout = Workout(
        workout_id,
        member_id,
        workout_date
    )

    list_exercises()

    exercise_name = input("Tên Exercise: ")

    sets = int(input("Sets: "))
    reps = int(input("Reps: "))
    weight = float(input("Weight: "))

    workout.add_exercise(
        exercise_name,
        sets,
        reps,
        weight
    )

    workout_service.add_workout(workout)

    print(f"Thêm Workout thành công! ID: {workout_id}")


def list_workouts():
    print("\n===== DANH SÁCH WORKOUT =====")

    workouts = workout_service.list_workouts()

    if not workouts:
        print("Chưa có workout.")
        return

    for workout in workouts:
        print(
            f"\nID: {workout.workout_id} | "
            f"Member: {workout.member_id} | "
            f"Ngày: {workout.date}"
        )

        for exercise in workout.exercises:
            print(
                f"  - {exercise['exercise']} | "
                f"{exercise['sets']} sets x "
                f"{exercise['reps']} reps | "
                f"Weight: {exercise['weight']} | "
                f"Volume: {exercise['volume']}"
            )


def workout_menu():
    while True:
        print("\n========== WORKOUT ==========")
        print("1. Thêm Workout")
        print("2. Danh sách Workout")
        print("0. Quay lại")

        choice = input("Nhập lựa chọn: ")

        if choice == "1":
            try:
                add_workout()
            except ValueError:
                print("Sets, Reps và Weight phải là số.")

        elif choice == "2":
            list_workouts()

        elif choice == "0":
            break

        else:
            print("Lựa chọn không hợp lệ!")


# =========================
# MEMBERSHIP
# =========================

def add_membership():
    print("\n===== ĐĂNG KÝ MEMBERSHIP =====")

    member_id = input("Member ID: ")
    membership_type = input("Loại gói: ")

    start_date_text = input("Ngày bắt đầu (YYYY-MM-DD): ")

    try:
        start_date = date.fromisoformat(start_date_text)
    except ValueError:
        print("Ngày không đúng định dạng.")
        return

    days = int(input("Số ngày sử dụng: "))
    price = float(input("Giá: "))

    end_date = start_date + timedelta(days=days)

    membership = Membership(
        member_id,
        membership_type,
        start_date,
        end_date,
        price
    )

    membership_service.add_membership(membership)

    print("Đăng ký Membership thành công!")


def list_memberships():
    print("\n===== DANH SÁCH MEMBERSHIP =====")

    memberships = membership_service.list_memberships()

    if not memberships:
        print("Chưa có membership.")
        return

    for membership in memberships:
        status = (
            "Hết hạn"
            if membership.is_expired()
            else "Đang hoạt động"
        )

        print(
            f"Member: {membership.member_id} | "
            f"Gói: {membership.membership_type} | "
            f"Từ: {membership.start_date} | "
            f"Đến: {membership.end_date} | "
            f"Giá: {membership.price} | "
            f"{status}"
        )


def membership_menu():
    while True:
        print("\n========== MEMBERSHIP ==========")
        print("1. Đăng ký Membership")
        print("2. Danh sách Membership")
        print("3. Membership đang hoạt động")
        print("0. Quay lại")

        choice = input("Nhập lựa chọn: ")

        if choice == "1":
            try:
                add_membership()
            except ValueError:
                print("Dữ liệu nhập không hợp lệ.")

        elif choice == "2":
            list_memberships()

        elif choice == "3":
            memberships = membership_service.list_active_memberships()

            if not memberships:
                print("Không có Membership đang hoạt động.")
            else:
                for membership in memberships:
                    print(
                        f"Member: {membership.member_id} | "
                        f"Gói: {membership.membership_type} | "
                        f"Đến: {membership.end_date}"
                    )

        elif choice == "0":
            break

        else:
            print("Lựa chọn không hợp lệ!")


# =========================
# PAYMENT
# =========================

def process_payment():
    print("\n===== THANH TOÁN =====")
    print("1. Tiền mặt")
    print("2. Thẻ")

    choice = input("Chọn phương thức: ")

    if choice == "1":
        payment = CashPayment()

    elif choice == "2":
        payment = CardPayment()

    else:
        print("Phương thức không hợp lệ.")
        return

    result = payment_service.process_payment(payment)

    print(result)


def list_payments():
    print("\n===== LỊCH SỬ THANH TOÁN =====")

    payments = payment_service.list_payments()

    if not payments:
        print("Chưa có giao dịch.")
        return

    for i, payment in enumerate(payments, start=1):
        print(f"{i}. {payment.process()}")


def payment_menu():
    while True:
        print("\n========== PAYMENT ==========")
        print("1. Thanh toán")
        print("2. Lịch sử thanh toán")
        print("0. Quay lại")

        choice = input("Nhập lựa chọn: ")

        if choice == "1":
            process_payment()

        elif choice == "2":
            list_payments()

        elif choice == "0":
            break

        else:
            print("Lựa chọn không hợp lệ!")


# =========================
# PROGRESS
# =========================

def show_progress():
    print("\n===== THEO DÕI PROGRESS =====")

    workouts = workout_repository.get_all()

    if not workouts:
        print("Chưa có workout để theo dõi.")
        return

    progress_service = ProgressService(workouts)

    weekly_volume = progress_service.calculate_weekly_volume()

    for week, exercises in weekly_volume.items():
        print(f"\n{week}")

        for exercise, volume in exercises.items():
            print(
                f"  {exercise}: {volume} kg"
            )


# =========================
# MAIN MENU
# =========================

def main():
    while True:
        print("\n========================================")
        print("       🏋️ FITTRACK MANAGEMENT")
        print("========================================")
        print("1. Quản lý Member")
        print("2. Quản lý Trainer")
        print("3. Quản lý Exercise")
        print("4. Quản lý Workout")
        print("5. Quản lý Membership")
        print("6. Thanh toán")
        print("7. Theo dõi Progress")
        print("0. Thoát")

        choice = input("Nhập lựa chọn: ")

        if choice == "1":
            member_menu()

        elif choice == "2":
            trainer_menu()

        elif choice == "3":
            exercise_menu()

        elif choice == "4":
            workout_menu()

        elif choice == "5":
            membership_menu()

        elif choice == "6":
            payment_menu()

        elif choice == "7":
            show_progress()

        elif choice == "0":
            print("\nCảm ơn bạn đã sử dụng FitTrack!")
            break

        else:
            print("Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    main()