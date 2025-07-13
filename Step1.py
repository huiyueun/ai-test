std::vector<Accessibility::Relation> GetAccessibilityRelations(Toolkit::Control control)
{
  const auto& relationMap = GetControlImplementation(control).mAccessibilityProps.relations;
  std::vector<Accessibility::Relation> result;

  for(const auto& relation : relationMap)
  {
    Accessibility::Relation newRelation(relation.first, {});

    for(const auto& weakActor : relation.second)
    {
      if(auto actor = weakActor.GetHandle())
      {
        if(auto accessible = Accessibility::Accessible::Get(actor))
        {
          newRelation.mTargets.push_back(accessible);
        }
      }
    }

    if(!newRelation.mTargets.empty())
    {
      result.emplace_back(std::move(newRelation));
    }
  }

  return result;
}
