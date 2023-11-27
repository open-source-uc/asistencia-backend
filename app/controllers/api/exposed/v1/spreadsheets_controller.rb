class Api::Exposed::V1::SpreadsheetsController < Api::Exposed::V1::BaseController
  def index
    respond_with activity_student_map
  end

  private

  def course
    @course ||= current_user.courses.friendly.find(params[:course_id])
  end

  def activities
    @activities ||= course.activities.where(slug: params[:activity_slugs])
  end

  def students
    @students ||= course.students.for_attendance_codes(params[:student_codes])
  end

  def activity_student_map
    activities.uniq.map do |activity|
      students_present = activity.attendances.where(student: students).map(&:student).uniq
      [activity.slug, students_present.map(&:attendance_codes)]
    end.to_h
  end

  def user
    @user ||= current_user
  end

  def spreadsheet_params
    params.permit(
      student_codes: [],
      activity_slugs: []
    )
  end
end
