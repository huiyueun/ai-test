std::vector<Accessibility::Relation> GetAccessibilityRelations(Toolkit::Control control)
{
  auto& relationMap = GetControlImplementation(control).mAccessibilityProps.relations;
  std::vector<Accessibility::Relation> result;

  for (auto& [relationType, targets] : relationMap)
  {
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

    // 무효한 weak handle 제거
    std::erase_if(targets, [](const auto& weakActor) {
      auto actor = weakActor.GetHandle();
      return !actor || !Accessibility::Accessible::Get(actor);
    });

    if (!newRelation.mTargets.empty())
    {
      result.emplace_back(std::move(newRelation));
    }
  }

  return result;
}
