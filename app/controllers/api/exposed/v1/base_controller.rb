class Api::Exposed::V1::BaseController < Api::Exposed::BaseController
  before_action do
    self.namespace_for_serializer = ::Api::Exposed::V1
  end
end
