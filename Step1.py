std::vector<Accessibility::Relation> GetAccessibilityRelations(Toolkit::Control control)
{
  auto& relationMap = GetControlImplementation(control).mAccessibilityProps.relations;
  std::vector<Accessibility::Relation> result;

  for (auto& relationPair : relationMap)
  {
    auto& relationType = relationPair.first;
    auto& targets = relationPair.second;

    Accessibility::Relation newRelation(relationType, {});

    for (auto it = targets.begin(); it != targets.end(); )
    {
      auto actor = it->GetHandle();
      auto accessible = actor ? Accessibility::Accessible::Get(actor) : nullptr;

      if (!accessible)
      {
        it = targets.erase(it);  // 무효한 weak handle 제거
      }
      else
      {
        newRelation.mTargets.push_back(accessible);
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
