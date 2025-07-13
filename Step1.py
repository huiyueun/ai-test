std::vector<Accessibility::Relation> GetAccessibilityRelations(Toolkit::Control control)
{
  auto& relationMap = GetControlImplementation(control).mAccessibilityProps.relations;
  std::vector<Accessibility::Relation> result;

  for (auto& relationPair : relationMap)
  {
    auto& relationType = relationPair.first;
    auto& targets = relationPair.second;

    Accessibility::Relation newRelation(relationType, {});

    for (const auto& weakActor : targets)
    {
      if (auto actor = weakActor.GetHandle())
      {
        if (auto accessible = Accessibility::Accessible::Get(actor))
        {
          newRelation.mTargets.push_back(accessible);
        }
      }
    }

    // C++17에서는 std::erase_if가 없으므로 반복문으로 제거
    for (auto it = targets.begin(); it != targets.end(); )
    {
      auto actor = it->GetHandle();
      if (!actor || !Accessibility::Accessible::Get(actor))
      {
        it = targets.erase(it);  // 무효한 weak handle 제거
      }
      else
      {
        ++it;
      }
    }

    if (!newRelation.mTargets.empty())
    {
      result.emplace_back(std::move(newRelation));
    }
  }

  return result;
}
